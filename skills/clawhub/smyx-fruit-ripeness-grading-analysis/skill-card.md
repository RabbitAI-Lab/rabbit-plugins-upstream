## Description:

Grades tomato and strawberry fruit ripeness from images or videos by analyzing visual cues such as color, colored-area ratio, gloss, and relative size, then returning a structured maturity grade and harvest-window guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, greenhouse operators, cooperatives, and agents supporting agricultural workflows use this skill to assess tomatoes or strawberries from uploaded media and produce ripeness grades, structured results, report links, and cloud-backed history lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files or private media URLs may be sent to the Life Emergence cloud service for analysis.

Mitigation: Avoid sensitive images and private internal URLs unless the publisher clarifies retention, processing, and deletion behavior.

Risk: The skill can query cloud report history and silently create or reuse a user identity.

Mitigation: Review account creation and report-history access behavior before deployment, and restrict use to the intended workspace or account.

Risk: A local workspace database may retain generated or reused identity tokens.

Mitigation: Inspect and manage local token storage according to organizational policy before sharing or archiving the workspace.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fruit-ripeness-grading-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted structured analysis text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include report links and cloud-backed history lists; default detail level is json.]

## Skill Version(s):

1.0.8 (source: server release metadata; SKILL.md frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
