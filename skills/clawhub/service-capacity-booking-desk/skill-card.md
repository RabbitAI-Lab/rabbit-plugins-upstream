## Description:

Select capacity windows and record capacity ledger entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and service planning teams use this skill to select a timezone-aware service capacity window and record the resulting capacity ledger entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ledger-recording stage can create capacity entries in the wrong scope if the backing tool is connected to an unintended capacity ledger.

Mitigation: Confirm before installation that the select and record tools are scoped to the intended service capacity ledger.

Risk: Recording a capacity-window entry may reserve or document capacity without the level of workflow approval the organization expects.

Mitigation: Require the appropriate user approval for creating capacity entries before enabling the record_capacity_window stage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/service-capacity-booking-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Structured text fields and JSON-like objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a capacity_window date-time and a capacity_ledger_entry object when the corresponding stage is invoked.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
