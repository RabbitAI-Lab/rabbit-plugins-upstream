## Description:

Guides agents in connecting to Typeform through Maton to manage forms, retrieve responses, and view insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Typeform can ask an agent to list or create forms, review survey responses and insights, or configure approved automations through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account may expose Typeform data beyond the immediate task.

Mitigation: Authorize only the scopes needed and prefer read-only access where possible.

Risk: Writes, deletions, and hosted automations can change data or run without further prompts.

Mitigation: Confirm each write or deletion and obtain approval before creating or running automation.

Risk: Trigger destinations can continuously forward event data to external hosts.

Mitigation: Keep destinations on Maton-controlled URLs unless the user explicitly approves a specific external host.

## Reference(s):

- [Typeform skill release](https://clawhub.ai/byungkyu/skills/typeform)
- [Maton homepage](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Typeform API overview](https://www.typeform.com/developers/get-started)
- [Typeform responses reference](https://www.typeform.com/developers/responses/reference/retrieve-responses)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and an authorized Typeform connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
