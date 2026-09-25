## Description:

Identifies individual cats from face images or videos by comparing them with previously registered cats and provides analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Cat owners and developers use this skill to distinguish individual cats in images or videos and review previous recognition reports. Cats must be registered before they can be matched.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cat images or videos and report-history requests are sent to the Life Emergence cloud service.

Mitigation: Use only media and report requests you are comfortable sharing with that service.

Risk: The skill silently creates or reuses a local identity and stores backend tokens in the workspace, allowing persistent account linkage.

Mitigation: Review or clear the workspace data directory if persistent account linkage is unwanted.

Risk: Cloud report history can be queried with limited user control.

Mitigation: Use the skill only when cloud history access is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-cat-face-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown report list; optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links or save results to a file.]

## Skill Version(s):

1.0.10 (source: ClawHub release; bundled SKILL.md states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
