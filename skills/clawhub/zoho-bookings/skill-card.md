## Description:

Helps agents manage Zoho Bookings appointments, services, staff, and workspaces through a Maton-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People managing a Zoho Bookings account can ask an agent to check availability and appointments or manage services, staff, and workspaces. Approved connections, functions, and triggers can also support ongoing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Appointment changes or other writes could modify the wrong booking or account.

Mitigation: Confirm each write and appointment change with the user and check the intended connection before acting.

Risk: Exposing a raw API key could grant unintended access to the connected account.

Mitigation: Prefer OAuth through the Maton CLI; avoid raw API keys when possible and do not disclose credentials.

Risk: Hosted functions, triggers, or destinations may continue acting or forwarding data without further prompts.

Mitigation: Get explicit approval for each automation and destination, limit its scope, and review or remove it when no longer needed.

## Reference(s):

- [Zoho Bookings skill on ClawHub](https://clawhub.ai/byungkyu/skills/zoho-bookings)
- [Maton](https://maton.ai)
- [Zoho Bookings API documentation](https://www.zoho.com/bookings/help/api/v1/oauthauthentication.html)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include booking details, availability, and instructions for approved changes or automations.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
