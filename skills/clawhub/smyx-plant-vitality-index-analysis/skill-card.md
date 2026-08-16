## Description:

Using plant images, optional environmental data, and growth metrics, this skill calls a cloud analysis service to produce a 0-100 plant vitality score, vitality grade, and trend for plant monitoring workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate plant vitality from images, videos, or report history and receive a structured score, grade, trend, and report link. It is intended for smart planters, plant factories, home gardening, and plant-monitoring platforms where users need concise plant health tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, and report history are sent to configured lifeemergence.com cloud services for analysis and history lookup.

Mitigation: Install and use the skill only when that cloud transfer is acceptable for the data being analyzed.

Risk: The skill can create or reuse a local workspace identity and store returned account tokens in a local SQLite database.

Mitigation: Review the local identity and token-storage behavior before installation, and run it only in a workspace where this persistence is acceptable.

## Reference(s):

- [Plant Vitality Index API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with a plant vitality score, trend, status fields, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a user-specified file when the CLI output path is provided.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
