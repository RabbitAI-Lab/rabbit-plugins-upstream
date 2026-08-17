## Description:

Researches relationships among industries, trade shows, associations, events, and companies using traceable public evidence, with explicit source-strength, participant-role, and list-completeness labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaynpeng](https://clawhub.ai/user/zaynpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Business researchers, market analysts, and sales operations teams use this skill to map public industry relationships by trade show, association, event, company, region, and time range. It is intended to support evidence-backed research, not to rank prospects or infer purchasing intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to inspect broad connected private business sources without tight user-controlled scoping.

Mitigation: Limit use to public web sources and explicitly selected local files unless private context is necessary and the agent is clearly instructed which sources it may read.

Risk: Public co-attendance, membership, or exhibitor evidence could be overread as sales priority or purchasing intent.

Mitigation: Use the skill's role, source-strength, list-completeness, and boundary labels, and require separate human review before using results for sales prioritization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-networkmap)
- [Publisher profile](https://clawhub.ai/user/zaynpeng)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with concise conclusions, scoped assumptions, and evidence tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records source strength, participant role, list completeness, evidence limits, and unconfirmed items.]

## Skill Version(s):

1.0.0 (source: release evidence and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
