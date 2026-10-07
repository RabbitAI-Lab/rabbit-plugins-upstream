## Description:

Turns project intake notes into delivery ledger entries, writes a local record, and optionally submits it to a configured delivery endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and implementation teams use this skill to extract a project code from a handoff note, create a delivery ledger entry, and optionally submit the record to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can trigger automatic external submission of delivery records.

Mitigation: Review the delivery endpoint and API key environment variables before execution; run without delivery configuration when external submission is not intended.

Risk: The skill creates local delivery ledger files.

Mitigation: Choose and review the output directory before running the skill.

## Reference(s):

- [Project Intake Identifier on ClawHub](https://clawhub.ai/wxt-ai/skills/project-code-notes-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local JSON Lines ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local record and delivery receipts; external submission occurs only when configured.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
