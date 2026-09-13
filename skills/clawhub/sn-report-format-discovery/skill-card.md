## Description:

Determines a short final-deliverable format label for a research request when the user asks for a recommendation or the desired output form is unclear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Research agents and workflow builders use this skill to choose a concise output format such as report, paper, table, memo, timeline, or FAQ while preserving the original request scope and language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected format label could steer downstream research output away from the user's intended deliverable.

Mitigation: Honor any explicit user-specified final form, keep the original query unchanged, and fall back to `report` only when the format cannot be determined.

Risk: Operators who do not read Chinese may miss the skill's narrow behavior constraints.

Mitigation: Review the Chinese skill instructions during deployment and confirm the agent only returns the short format label.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-report-format-discovery)
- [Publisher profile](https://clawhub.ai/user/sensenova-skills)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Single-line text in the form `format: <short non-empty string>`]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not create files, schemas, candidate objects, or external-format lookups.]

## Skill Version(s):

2026.9.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
