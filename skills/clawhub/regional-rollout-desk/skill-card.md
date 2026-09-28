## Description:

Select rollout regions and register deployment brief records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations teams use this skill to select a deployment region from a rollout request and to record the selected region in a deployment brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may request the wrong stage or leave the intended stage ambiguous.

Mitigation: Ask explicitly whether the task is region selection or deployment-region registration before invoking the skill.

Risk: Region selection depends on the supplied residency information and may be incomplete when the request lacks that input.

Mitigation: Confirm required residency details before using the selected region in a deployment brief.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/regional-rollout-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [String or JSON object in the requested output field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are concise deployment-region values or recorded-region brief objects.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
