## Description:

Add entries to a renewal schedule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agreement operations teams use this skill to turn supplied renewal-obligation data into a concise schedule receipt for a renewal handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expect the skill to update a real renewal calendar or external system.

Mitigation: Treat the output as a schedule receipt generated from supplied data unless a separate reviewed integration is added.

Risk: Supplying unnecessary agreement data can expose more business information than the workflow needs.

Mitigation: Provide only the agreement_id and obligation rows needed for the renewal schedule request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/agreement-renewal-schedule-workbench)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise schedule receipt object with schedule_id and rows, typically returned in text or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the obligation_schedule object supplied in the current request and does not require credentials, private files, network access, persistence, or command execution.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
