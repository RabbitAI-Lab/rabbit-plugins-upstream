## Description:

Analyzes rehab training video or image inputs to identify frustration or giving-up tendency signals and return structured motivation recommendations, escalation guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External rehab care teams, home rehab operators, or agents supporting them use this skill to analyze fixed-camera training media for frustration cues, lack-of-progress patterns, and motivation workflow recommendations. It supports structured reporting and history review without making medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive rehab patient video or audio may be processed by a cloud service.

Mitigation: Deploy only with patient consent, approved camera or storage sources, and clear retention and access controls.

Risk: Identity-linked report history and local account tokens may persist across runs.

Mitigation: Use managed environments with restricted filesystem access, token handling controls, and documented cleanup for shared systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-style text reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links, structured analysis fields, and history tables.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
