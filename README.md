# Tau Core Technical Paper II

**Foundation-series position:** Paper III

## Complete Record Edges, Path Holonomy, and Recovery-Correctable Readouts

This repository contains the reviewer-facing technical manuscript and
reproducibility package for Tau Core Technical Paper II (series Paper III).

The current reviewer manuscript is 15 A4 pages.  Its opening series map and
notation ledger make explicit that frozen source identification precedes
record transport and cannot be inferred backward from recovery success.

The manuscript follows the source-signature analysis of Technical Paper I
(series Paper II) and distinguishes state-family, operator-system,
correctable-algebra and
full-code recovery. For approximate recovery it proves
an explicit Uhlmann-chord loss bound from a trace-norm or diamond-norm error
certificate. The finite body-action identification remains a separate open
Tau-specific input.

A later enriched-source backport sharpens that boundary. On the adopted
primary ROOT branch, a traced two-leg source, the canonical represented trace
and the primitive-extensive finite Trace--Gram law are conditionally
constructed. Cyclic generated support and stable record existence select the
complete source packet inside the declared source-irredundant MVP class. They
do not certify complete-edge invertibility, exact recovery, a laboratory
carrier, or selection over unrestricted rank-novel parent alternatives.

The paper isolates the finite record-transport layer that was too detailed for
Foundation Paper I.

## Observer Co-Descent

Record edges operate inside the inherited observer co-descent architecture.
The observer is not a detached endpoint: occupied carrier support, regular
local rank four, stable quantization and a nonzero record/effect jointly make
it operational and co-produce its accessible 4D world. Transport success does
not create the body or an independent channel layer.

## Atemporal Parent-Realization Terminology

Because the Tau parent is atemporal, “Nature selects” does not mean an
external agent or a later decision. It is legacy shorthand for the internal
physical implication

\[
(B_\tau^{\mathrm{phys}},s_U,\mathcal L_{\mathrm{parent}})
\Longrightarrow \mathfrak P,
\]

together with physical occupation of the support of \(\mathfrak P\). A theorem
inside a declared completion proves only class-relative realization; it does
not prove this unrestricted base–seed arrow. Agreement of finitely many
terminal readouts also cannot establish ambient-source exhaustivity. The
current terminology is therefore **parent-law realization** and **physical
occupation**.

## Results

- reversible complete source-owned record edges;
- exact finite Trace--Gram transport on their occupied support;
- pathwise composition and descriptor-frozen holonomy;
- irreversible CP maps with an exact recovery;
- a three-qubit recovery-correctable toy construction;
- the commuting-record reversibility no-go;
- a quantitative partial-dephasing control invisible to diagonal records;
- a carrier-class evidence table and a typed proof/falsification dependency;
- the strengthened `FOC-7` occupation certificate.

The paper now places record transport explicitly inside the common law
`Y_O^(a)=Q_O^(a) o T^(a) o A_O[M_tau]`: record formation is the finite
resolution/acceptance stage after morphology-conditioned observer access and
typed terminal precursors, not an independent ontological layer.

## Claim Boundary

The isolation boundary is now explicit: source-component separation plus a
disjoint-source valuation yields exact protected transport; crossing source
incidence permits irreversible local behavior. Physical realization of the
valuation is not claimed.

This is a mathematical foundations paper. It does **not** prove that the
unrestricted physical parent law realizes or occupies complete record edges,
identify a physical Tau carrier,
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
