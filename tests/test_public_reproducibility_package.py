from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "paperIII_submission_source" / "main.tex"


def test_required_files_exist():
    for path in [
        ROOT / "README.md",
        ROOT / "REVIEWER_READINESS.md",
        ROOT / "CITATION.cff",
        ROOT / "DATA_NOTICE.md",
        TEX,
        ROOT / "paperIII_submission_source" / "refs.bib",
        ROOT / "paperIII_submission_source" / "main.pdf",
        ROOT / "arxiv_submission_source.zip",
    ]:
        assert path.exists(), path


def test_claim_boundaries_and_results():
    text = TEX.read_text()
    normalized = " ".join(text.split())
    for marker in [
        "Foundation Paper III",
        "Exact finite identity on a complete edge",
        "Claim-complete operational descriptor",
        "Recovery sandwich",
        "Explicit approximate-recovery chord bound",
        "Recovery domains",
        "Exact recovery-correctable non-isomorphic edge",
        "Commuting-record reversibility no-go",
        "FOC-7 occupation certificate",
    ]:
        assert marker in text
    assert "do not prove that a physical parent source creates or occupies complete edges" in normalized
    lower = text.lower()
    for forbidden in [
        "tau core is empirically validated",
        "we prove that nature",
        "derives the standard model",
    ]:
        assert forbidden not in lower


def test_recovery_toy_syndromes_and_identity():
    code = {0: "000", 1: "111"}
    seen = set()
    for error in [None, 0, 1, 2]:
        words = []
        for bit in [0, 1]:
            chars = list(code[bit])
            if error is not None:
                chars[error] = "1" if chars[error] == "0" else "0"
            words.append("".join(chars))
        syndrome = tuple(words)
        assert syndrome not in seen
        seen.add(syndrome)
    assert len(seen) == 4


def test_finite_response_countermodel():
    y1, y2, lam = 0.2, 0.3, 0.7
    f = lambda y: y + lam * y**2
    defect = f(y1 + y2) - f(y1) - f(y2)
    assert abs(defect - 2 * lam * y1 * y2) < 1e-12


def test_approximate_recovery_bound_is_nonnegative_and_exact_at_zero():
    def loss_bound(x_in, eta):
        return x_in - max(0.0, x_in**0.5 - 2 * eta**0.5) ** 2

    assert abs(loss_bound(0.7, 0.0)) < 1e-12
    for x_in in [0.0, 0.01, 0.5, 2.0]:
        for eta in [0.0, 1e-4, 0.02, 0.5]:
            bound = loss_bound(x_in, eta)
            assert -1e-12 <= bound <= x_in + 1e-12


def test_figures_and_arxiv_source():
    text = TEX.read_text()
    for name in ["fig_edge_branch.pdf", "fig_holonomy_triangle.pdf"]:
        assert name in text
        assert (ROOT / "paperIII_submission_source" / "figures" / name).exists()
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as archive:
        names = archive.namelist()
    assert "main.tex" in names
    assert "refs.bib" in names
    assert "main.pdf" not in names
    assert all(not name.endswith(".aux") for name in names)
