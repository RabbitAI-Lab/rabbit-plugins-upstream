## Description:

Analyzes multi-day fixed home-camera video from bedroom and dining areas to report long immobility, appetite-related eating changes, and behavior-change alerts for elder-care monitoring without making a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, care teams, and developers can use this skill to summarize long-duration home-camera observations for elderly or solo-living individuals. It supports behavior-change monitoring and family or community-care alerts, while leaving diagnosis and treatment decisions to qualified clinicians.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can process sensitive home surveillance media or media URLs through lifeemergence.com cloud services.

Mitigation: Use only with explicit informed consent, confirm that the cloud provider and retention model are acceptable, and avoid submitting media outside the intended elder-care monitoring context.

Risk: The skill can create or reuse an internal account identity and store access tokens in the local workspace.

Mitigation: Install only in workspaces where local account and token storage is acceptable, and review workspace access controls before use.

Risk: Behavioral markers may be mistaken for a medical diagnosis.

Mitigation: Present outputs as behavioral observations and care prompts only; route diagnosis, treatment, medication, and crisis decisions to qualified clinicians or emergency resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports, including behavior metrics, alert text, suggested actions, and report links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [History report queries return cloud-sourced report lists; analysis outputs depend on 24-hour or longer bedroom and dining-area video coverage and baseline availability.]

## Skill Version(s):

1.0.9 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
