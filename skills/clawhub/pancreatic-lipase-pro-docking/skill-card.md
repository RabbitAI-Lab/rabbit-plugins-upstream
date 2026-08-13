## Description:

Professional virtual-screening stack for human pancreatic lipase PDB 1LPB that prepares ligands, performs local multi-site molecular docking, validates outputs, and builds reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, researchers, educators, and computational chemistry teams use this skill to run authorized virtual screens against human pancreatic lipase, inspect docking scores, and generate local reports. Results are computational predictions and should be reviewed before use in scientific or operational decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup and bootstrap paths may install scientific dependencies and use local compute resources.

Mitigation: Run in a dedicated project directory or environment, avoid sudo, and review setup scripts and outputs before relying on them.

Risk: Optional public molecule or receptor lookups can disclose ligand names or SMILES to public services.

Mitigation: Do not submit confidential compounds to public lookup services unless that disclosure is acceptable; provide local input files when confidentiality matters.

Risk: Logs, result files, and reports may contain user-supplied ligand names, SMILES, scores, and derived analysis.

Mitigation: Store generated outputs in a controlled workspace, review them before sharing, and protect logs that contain sensitive project data.

Risk: Docking scores and ranked hits are computational predictions.

Mitigation: Validate results experimentally or through an appropriate scientific review process before using them for decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/pancreatic-lipase-pro-docking)
- [Artifact README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [PubChem PUG REST Endpoint](https://pubchem.ncbi.nlm.nih.gov/rest/pug)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown, Files]

**Output Format:** [Markdown guidance with bash commands plus generated local CSV, log, HTML, and Markdown report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally in a user-provided project environment; pipeline outputs are written under local run directories and may include ligand names, SMILES, docking scores, logs, dashboards, and reports.]

## Skill Version(s):

100.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
