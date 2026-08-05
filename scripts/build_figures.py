#!/usr/bin/env python3
from pathlib import Path
import shutil

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
SRC_OUT = ROOT / "paperII_submission_source" / "figures"


def box(ax, xy, width, height, text, color):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        linewidth=1.4,
        edgecolor="#20252b",
        facecolor=color,
    )
    ax.add_patch(patch)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=9)


def arrow(ax, start, end, label=""):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=12, linewidth=1.3,
                                color="#263238"))
    if label:
        ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + 0.035,
                label, ha="center", va="bottom", fontsize=8)


def build_branch_figure(path):
    fig, ax = plt.subplots(figsize=(7.4, 3.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    box(ax, (0.04, 0.39), 0.20, 0.22, "occupied\nrecord packet", "#dceef8")
    box(ax, (0.39, 0.67), 0.25, 0.20, "reversible complete edge\ntrace-preserving *-isomorphism", "#dff3e4")
    box(ax, (0.73, 0.67), 0.23, 0.20, "exact Trace-Gram\nfinite A8b", "#eef6d8")
    box(ax, (0.39, 0.13), 0.25, 0.20, "irreversible CP edge\nrecovery required", "#fde5d6")
    box(ax, (0.73, 0.13), 0.23, 0.20, "exact equality or\ncontraction/finite defect", "#f7dfdf")
    arrow(ax, (0.24, 0.53), (0.39, 0.76), "source selection")
    arrow(ax, (0.24, 0.47), (0.39, 0.24), "source selection")
    arrow(ax, (0.64, 0.77), (0.73, 0.77), "extensivity")
    arrow(ax, (0.64, 0.23), (0.73, 0.23), "recovery test")
    ax.text(0.5, 0.97, "The finite physical fork", ha="center",
            va="top", fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def build_holonomy_figure(path):
    fig, ax = plt.subplots(figsize=(6.2, 4.1))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    points = {"u": (0.15, 0.18), "v": (0.50, 0.82), "w": (0.85, 0.18)}
    for name, (x, y) in points.items():
        ax.scatter([x], [y], s=520, color="#e8eef2", edgecolor="#263238", zorder=3)
        ax.text(x, y, name, ha="center", va="center", fontsize=13, fontweight="bold")
    arrow(ax, (0.19, 0.24), (0.46, 0.75), "Ad_X")
    arrow(ax, (0.54, 0.75), (0.81, 0.24), "Ad_X")
    arrow(ax, (0.22, 0.16), (0.78, 0.16), "Ad_Z")
    ax.text(0.50, 0.04, "relative holonomy Ad_Z: null on diagonal records,\nvisible on coherent X-basis records",
            ha="center", va="bottom", fontsize=9)
    ax.text(0.5, 0.98, "Three-vertex descriptor-frozen holonomy control",
            ha="center", va="top", fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    SRC_OUT.mkdir(parents=True, exist_ok=True)
    paths = [
        OUT / "fig_edge_branch.pdf",
        OUT / "fig_holonomy_triangle.pdf",
    ]
    build_branch_figure(paths[0])
    build_holonomy_figure(paths[1])
    for path in paths:
        shutil.copy2(path, SRC_OUT / path.name)
    print("WROTE", *paths)


if __name__ == "__main__":
    main()
