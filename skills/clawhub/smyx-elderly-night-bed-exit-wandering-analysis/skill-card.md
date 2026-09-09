## Description:

Analyzes fixed night-vision bedroom or hallway camera footage to detect elderly bed-exit duration, wandering behavior, and threshold-based alerts for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External care teams, nursing-home operators, and home-care developers use this skill to analyze night-vision bedroom or hallway footage for bed-exit duration, wandering behavior, and threshold-based alerts. The skill provides behavior statistics and alerts, not medical diagnosis or care instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags sensitive bedroom-video cloud analysis with broad automatic identity, credential persistence, and under-scoped network behavior.

Mitigation: Install only after the publisher documents what footage and report data are sent to remote services, obtains explicit consent for video upload and history retrieval, and limits the skill to trusted destinations.

Risk: The security guidance says the release configuration must require HTTPS and restrict trusted destinations.

Mitigation: Use only HTTPS service endpoints in release configuration and block local, test, or plaintext HTTP destinations before deployment.

Risk: The security guidance warns against storing tokens in a shared plaintext database.

Mitigation: Store tokens in a protected credential store and rotate any credentials that may have been persisted by earlier runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-night-bed-exit-wandering-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown text with structured JSON analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bed-exit events, total bed-exit duration, wandering detection, alert level, alert message, and report export links.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
