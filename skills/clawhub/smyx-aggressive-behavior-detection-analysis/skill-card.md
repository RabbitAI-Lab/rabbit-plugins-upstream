## Description:

Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing and butting, and outputs behavior type, intensity level and alert level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, developers, and external users use this skill to analyze livestock or poultry barn images and videos for aggressive behaviors, produce structured findings, and review alert levels and historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media or media URLs are sent to Life Emergence/Open API services for remote analysis.

Mitigation: Install only when this data flow is acceptable, and confirm provider retention and account policies before using sensitive footage.

Risk: The skill creates or reuses a local identity and may store authentication tokens in a workspace SQLite database.

Mitigation: Use a separate workspace or disposable identity when containment is required, and review local storage before deployment.

Risk: The security verdict is suspicious because identity and token handling deserve user review.

Mitigation: Review and scan the skill before deployment, and limit use to trusted environments until the risk is accepted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis reports, Markdown history tables, and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes behavior type, timestamps or report rows, subject locations when available, intensity level, alert level, and report links.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
