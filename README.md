# Tau Core Foundation Paper III

## Complete Record Edges, Path Holonomy, and Recovery-Correctable Readouts

This repository contains the reviewer-facing technical manuscript and
reproducibility package for Tau Core Foundation Paper III.

The current reviewer manuscript is 13 A4 pages.

The manuscript follows the source-signature analysis of Foundation Paper II
and distinguishes state-family, operator-system, correctable-algebra and
full-code recovery. For approximate recovery it proves
an explicit Uhlmann-chord loss bound from a trace-norm or diamond-norm error
certificate. The finite body-action identification remains a separate open
Tau-specific input.

The paper isolates the finite record-transport layer that was too detailed for
Foundation Paper I. It proves conditional internal results for:

- reversible complete source-owned record edges;
- exact finite Trace--Gram transport on their occupied support;
- pathwise composition and descriptor-frozen holonomy;
- irreversible CP maps with an exact recovery;
- a three-qubit recovery-correctable toy construction;
- the commuting-record reversibility no-go;
- a quantitative partial-dephasing control invisible to diagonal records;
- a carrier-class evidence table and a typed proof/falsification dependency;
- the strengthened `FOC-7` occupation certificate.

## Claim Boundary

This is a mathematical foundations paper. It does **not** prove that Nature
creates or occupies complete record edges, identify a physical Tau carrier,
derive the Standard Model, or provide empirical validation. The CP construction
is a toy model showing logical possibility, not a claimed physical realization.

## Reproduce

```bash
python3 scripts/reproduce.py
```

The command rebuilds the figures, PDF, deterministic arXiv source archive, and
runs the public tests.

## Outputs

- `paperIII_submission_source/main.pdf`
- `arxiv_submission_source.zip`
- `data/derived/recovery_toy_summary.json`
