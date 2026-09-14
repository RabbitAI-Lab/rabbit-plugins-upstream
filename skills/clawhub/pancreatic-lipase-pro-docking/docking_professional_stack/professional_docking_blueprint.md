# Professional Molecular Docking Blueprint

This is the reusable operating protocol I should follow whenever asked to perform docking or virtual screening.

## Core rule
Docking is not proof of biological activity. A professional answer must combine receptor validity, ligand preparation, protocol validation, docking score, pose quality, interaction analysis, physicochemical/ADMET filters, and uncertainty.

---

## 1. Clarify the job
Ask only if missing information blocks the work.

Minimum needed:
- Target protein or PDB ID
- Ligands as SMILES/SDF/MOL2/CSV, or permission to use demo/known ligands
- Species if biologically important
- Desired depth: fast, standard, validated, MD/free-energy

If the user gives no receptor:
- Select a well-supported public structure.
- Explain why.

If the user gives no ligands:
- Do not invent final scientific claims.
- Use demo controls only for workflow demonstration.

---

## 2. Receptor selection
Professional checks:
- Correct species and isoform
- Crystal/cryo-EM resolution
- Ligand-bound vs apo
- Open/closed conformation
- Missing residues/atoms
- Cofactors, metals, waters, prosthetic groups
- Active-site accessibility
- Literature relevance

For pancreatic lipase default:
- Target: human pancreatic lipase
- Default PDB: 1LPB
- Binding-site default: co-crystallized ligand MUP centroid if available
- Catalytic triad: Ser152, Asp176, His263
- Important nearby residues often include Phe77, Leu153, Tyr114, Leu213, Phe215, Arg256, Leu264

---

## 3. Protein preparation
Required actions:
- Remove irrelevant crystallographic waters
- Keep structurally/catalytically important waters if justified
- Remove unrelated ligands unless used for grid definition or validation
- Add hydrogens
- Assign protonation states
- Check histidine tautomers
- Assign charges
- Repair missing side chains if needed
- Save prepared receptor and preparation notes

Report any uncertainty.

---

## 4. Ligand preparation
Required actions:
- Standardize structures
- Preserve stereochemistry
- Generate tautomers/protonation states when relevant
- Generate 3D conformers
- Energy-minimize conformers
- Assign charges
- Convert to docking format

Do not treat ambiguous SMILES as publication-grade input.

---

## 5. Protocol validation
Professional docking should include at least one validation if possible:

### Redocking
- Extract native ligand.
- Dock it back into the receptor.
- Calculate RMSD to crystal pose.
- RMSD <= 2.0 Å is usually acceptable.

### Controls
- Include known active ligand if available.
- Include weak/negative controls if available.

If validation fails, label predictions low-confidence.

---

## 6. Docking execution
Recommended engines:
- Open-source fast: AutoDock Vina, Smina, QuickVina
- ML-assisted: Gnina, DiffDock as complementary tools
- Commercial if user has access: Glide, GOLD, MOE

Professional behavior:
- Run ligands one-by-one for clean logs.
- Use reproducible parameters.
- Save poses and logs.
- Use multiple poses per ligand.
- For fast screens, use low exhaustiveness and clearly label approximate results.
- For standard screens, use higher exhaustiveness and repeatability checks.

---

## 7. Interaction analysis
Never rank only by docking score.

Check:
- Does the pose sit in the intended pocket?
- Does it contact catalytic/functional residues?
- Are H-bonds geometrically sensible?
- Are hydrophobic contacts plausible?
- Is the ligand strained or folded unrealistically?
- Does it clash with the protein?
- Is it outside the binding site despite a good score?

Useful tools:
- PLIP
- ProLIF
- RDKit
- MDAnalysis
- PyMOL/ChimeraX visual inspection

---

## 8. Parallel in silico filters
Run these alongside docking when possible:
- Molecular weight
- cLogP
- H-bond donors/acceptors
- TPSA
- Rotatable bonds
- Lipinski rules
- Veber rules
- PAINS/assay-interference alerts
- Aggregator risk if possible
- Solubility estimate
- GI absorption estimate
- CYP/hERG/hepatotoxicity warnings if tools are available

Natural products and polyphenols need extra false-positive caution.

---

## 9. Advanced professional layers
Use when requested or needed.

### Ensemble docking
Dock against:
- Multiple PDB structures
- Open/closed conformations
- MD snapshots
- Alternative protonation states

### Molecular dynamics
After docking:
- Run OpenMM/GROMACS/AMBER simulation
- Track ligand RMSD, protein RMSD, RMSF
- Track H-bond occupancy
- Track distance to key residues
- Check pose stability

### Rescoring
Use:
- MM/GBSA
- MM/PBSA
- Consensus scoring

### Free-energy methods
For close analogs:
- FEP/RBFE/TI/ABFE
- OpenFE, Perses, YANK, Schrödinger FEP+, AMBER/OpenMM workflows

### QM/QM-MM
Use for:
- Covalent inhibition
- Reaction mechanism
- Protonation/tautomer uncertainty
- Metal coordination
- Charge distribution

---

## 10. Ranking logic
Use consensus, not one score.

Suggested evidence weights for early screening:
- 35% docking score
- 25% pose/interactions with key residues
- 15% validation/control consistency
- 15% physicochemical/drug-likeness filters
- 10% ADMET/PAINS risk

For pancreatic lipase, prioritize:
- Favorable active-site pose near Ser152/Asp176/His263
- Occupation of hydrophobic pocket
- Interactions with Phe77/Leu153/Phe215/Arg256 region when relevant
- No severe PAINS/aggregator warning
- Plausible intestinal exposure profile

---

## 11. Reporting format
Every professional result should include:

| Compound | Docking score | Pose quality | Key interactions | Lipinski/Veber | PAINS/ADMET flags | Prediction | Confidence |
|---|---:|---|---|---|---|---|---|

Prediction labels:
- Strong predicted binder
- Moderate predicted binder
- Weak predicted binder
- Unreliable / likely false positive
- Undetermined

Confidence labels:
- High: validated protocol + good pose + controls + consistent filters
- Medium: good docking/pose but limited validation
- Low: unvalidated or conflicting evidence

Always include:
- Method summary
- Parameters
- Files generated
- Limitations
- Recommended experimental validation

---

## 12. Default fast workflow for pancreatic lipase
If the user asks for pancreatic lipase docking and provides ligands:

1. Use human pancreatic lipase PDB 1LPB unless user provides another receptor.
2. Define grid from MUP centroid; fallback to Ser152/Asp176/His263 centroid.
3. Prepare receptor and ligands.
4. Redock MUP if native ligand extraction is possible.
5. Dock each ligand with Vina/Smina/Gnina.
6. Run descriptors/PAINS in parallel.
7. Analyze key interactions.
8. Rank by consensus.
9. Report cautious predictions.

Fast command pattern:
```bash
python lipase_docking_fastkit.py --input ligands.csv --mode dock --exhaustiveness 4 --cpu 4
```

---

## 13. Scientific wording discipline
Use:
- "Predicted binder"
- "Candidate inhibitor"
- "Prioritized for experimental testing"
- "Docking suggests"

Avoid:
- "Proven inhibitor"
- "Definitely active"
- "IC50 is X" unless experimentally measured
- Overclaiming from a single score

Final reminder:
A professional computational docking answer is a reproducible, validated, uncertainty-aware prioritization workflow, not a single number.
