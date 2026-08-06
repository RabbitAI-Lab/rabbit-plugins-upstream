# 🧬 Pancreatic Lipase Pro Docking

**Category:** research

## ✨ What This Skill Does
Professional virtual-screening stack for human pancreatic lipase (PDB 1LPB). Multi-site molecular docking (catalytic triad, oxyanion hole, lid, etc.), molecule preparation, scoring, hit selection, and report generation.

## 🔐 Permissions & Requirements
• Requires conda environment with rdkit, meeko, vina, gemmi, openbabel
• Runs AutoDock Vina locally (CPU/GPU)
• Reads receptor PDB + ligand SDF/SMILES input
• May download molecules from PubChem (network)

## 🔒 Security & Privacy
  - Runs compute-heavy docking locally.
  - May fetch molecule data from PubChem; no sensitive data sent.
  - No secrets are involved.
  - Results are computational predictions — validate experimentally.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `dd6d4101f559e70c9f97a07e09fe851fca34d5b1da42ff5302fe19c6d8a33db7`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
