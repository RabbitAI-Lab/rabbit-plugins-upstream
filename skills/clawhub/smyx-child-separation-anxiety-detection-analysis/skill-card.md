## Description:

Using a fixed camera at the home entrance or kindergarten gate, the system analyzes pre-school videos and detects crying facial expressions, physical clinging actions, and resistance behaviors, then evaluates separation-anxiety levels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and early-childhood educators can use the skill to review drop-off videos for visible crying, clinging, and resistance behaviors and receive a structured observation with supportive suggestions. It is intended for early awareness and does not provide a psychological diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video files, which may show identifiable children, are uploaded to LifeEmergence services without local masking; the remote service's retention, deletion, and access protections were not verified.

Mitigation: Defer use with identifiable children's footage until upload behavior and credential protection are addressed. Obtain guardian authorization and confirm the provider's retention, deletion, and access policies before any permitted use.

Risk: The export-only option does not prevent video uploads, and the API URL option does not reliably change the upload destination.

Mitigation: Do not rely on either option to control data transfer; verify actual destinations and upload behavior before using any footage.

Risk: Account credentials are stored without adequate protection.

Mitigation: Avoid production use until credential storage is fixed, and protect any account credentials used in a controlled environment.

Risk: Visible crying or resistance can be misread, and an automated severity label could be mistaken for a psychological diagnosis.

Mitigation: Treat results as visual observations for early awareness, consider the surrounding context, and seek qualified professional assessment when concerns persist.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured behavior analysis reports, historical report tables, and supportive recommendations with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports assign a mild, moderate, or severe separation-anxiety level based on visual behavior cues; they are not a clinical diagnosis.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
