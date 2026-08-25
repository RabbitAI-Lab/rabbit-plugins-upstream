## Description:

Identifies plant growth stages from plant image or video inputs and returns structured analysis for precision agriculture decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural producers, agronomists, and developers use this skill to analyze plant images or videos, classify growth stages, review structured plant-status reports, and query prior cloud analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media, URLs, and report history are processed through external cloud services.

Mitigation: Use the skill only with inputs you are willing to send to the configured service, and verify the publisher's endpoint and retention practices before installation.

Risk: The skill may create or reuse local identity state, store tokens, and bootstrap backend account behavior without direct user prompts.

Mitigation: Review the skill before installing, run it in an isolated environment when evaluating it, and confirm account, billing, and local state behavior with the publisher.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Structured report text, JSON results, Markdown history tables, and script invocation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud report history returned by the configured service.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
