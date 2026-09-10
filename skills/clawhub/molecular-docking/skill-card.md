## Description:

Run and diagnose expert-grade protein-ligand molecular docking through SciMiner using Gnina, AutoDock Vina, PackDock, SurfDock, DiffDock, and fpocket.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciminer](https://clawhub.ai/user/sciminer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, computational chemists, and drug-discovery teams use this skill to run and diagnose protein-ligand docking through SciMiner, including engine selection, pose-pool analysis, clustering, and confidence grading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable remote SciMiner documentation controls endpoint, request, credential, and upload behavior during use.

Mitigation: Verify credentialed requests and file uploads stay on the intended SciMiner origin, and use endpoint allowlisting or equivalent controls where available.

Risk: The skill requires a SCIMINER_API_KEY and may submit molecular structure files to SciMiner services.

Mitigation: Use a scoped or short-lived API key where possible and avoid submitting confidential molecular structures unless the deployment environment enforces the required controls.

Risk: Docking results can be misleading if a single run, Rank 1 pose, or raw score is treated as a final answer.

Mitigation: Require multi-seed pose pooling, energy-gap filtering, RMSD clustering, recurrence checks, critical-contact review, and confidence grading before reporting a final docking hypothesis.

## Reference(s):

- [Molecular Docking Skill on ClawHub](https://clawhub.ai/sciminer/skills/molecular-docking)
- [SciMiner Tool API Documentation](https://sciminer.tech/tool_api_files/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown reports with command snippets, generated docking artifact references, and SciMiner history URLs when tasks succeed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes system audit, sampling manifest, pose-pool summary, cluster table, final decision, confidence level, and pose provenance details.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
