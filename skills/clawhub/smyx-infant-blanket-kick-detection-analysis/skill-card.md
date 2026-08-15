## Description:

Using a night-time camera (infrared or low-light) above the crib, the skill analyzes blanket coverage on an infant's body, detects low coverage or kicking motions that cause the blanket to slip off, and outputs an alert.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze infant crib night-time video or image inputs for blanket coverage, kicking events, blanket slippage, alert status, and prior report lookup. The results are auxiliary visual-monitoring outputs and are not a replacement for adult supervision or medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant crib videos, video URLs, analysis history requests, and related identity/account data may be sent to configured lifeemergence.com services.

Mitigation: Use only with guardian authorization and an approved data-handling plan; avoid unnecessary identifying content and confirm the external service is acceptable for the deployment.

Risk: The skill can silently create or reuse local identity state and store tokens in the workspace data directory.

Mitigation: Run the skill in an isolated workspace, restrict local file permissions, and clear local identity or token state when the analysis workflow is complete.

Risk: Blanket coverage alerts may be over-relied on for a sensitive infant-safety use case.

Mitigation: Treat outputs as auxiliary visual-monitoring signals; require adult verification for alerts and do not use the skill as medical advice or a substitute for supervision.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or JSON-style structured analysis text with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alert status, blanket coverage fields, event summaries, recommendations, report links, and historical report tables.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
