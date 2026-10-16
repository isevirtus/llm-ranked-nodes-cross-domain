# Confidence-guided Bayesian network parameterization

Private replication package for **Confidence-Guided Bayesian Network Parameterization with Language Models and Ranked Nodes: An Exploratory Study Across Two Domains**, prepared for ACM SAC 2027 (MLA).

## Reproduce

Clone or download this repository, then run:

```sh
python verify_package.py
```

This checks the replication ZIP's SHA-256, safely extracts it into a temporary directory, runs its numerical verifier, and writes the recomputed CSV files to `results/`.

To inspect all source files and notebooks directly, extract the package:

```sh
python -m zipfile -e replication-package.zip .
cd replication-package
python scripts/reproduce.py
```

Python 3.10+ is sufficient. The numerical reproduction uses only the standard library: no GPU, credentials, internet connection, or paid API is required.

The complete directory tree is distributed as a ZIP to preserve the original archive and notebook bytes. Its internal README documents figure generation and fresh-generation limitations. SHA256SUMS verifies the downloadable files.

## Included evidence

- Eight unchanged generation/evaluation archives and five original notebooks, with provenance and checksums.
- Reconstructed executed protocol, data dictionary through the original specifications, reproduction instructions, claim-to-result mapping, and limitations.
- Dependency-free verification of 16 generated networks and eight reconstructed persona pools against the original evaluator, plus two uniform baselines.
- Recomputed probability, row, node, routing, and aggregate diagnostics.
- Anonymous six-page MLA paper, LaTeX source, bibliography, and generated figures/tables.

The maximum observed discrepancy from the archived metrics is below 6.1e-10. Weighted BN KL reuses archived reference-parent marginals; it does not independently repeat BN inference. Each experimental cell has one generation; no significance or general model-superiority claim is supported.

## Findings

Results vary by domain and metric. The 4B equal pool has the lowest weighted BN KL in both domains, while **every electric-vehicle configuration has worse mean CPT KL than uniform probabilities**. The 9B model directly elicits more conditional rows, including highly confident, large reference disagreements. There is no direct-only or RN-only experimental arm.

## Review status

Keep this repository private during double-blind review. The manuscript excludes author names and this identifying repository URL. Original archives retain provenance and notebook metadata and require a separately inspected anonymous version before reviewer distribution. No blanket license is asserted for the original study material; see THIRD_PARTY_NOTICES.md inside the package.

No new LLM generations were run while preparing the package. The prior software-engineering manuscript is backed up separately and excluded here.
