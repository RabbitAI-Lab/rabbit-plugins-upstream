## Description:

Query and update Zola wedding-planning data directly from a shell using curl against Zola's mobile API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-focused users use this skill to inspect and manage Zola wedding data such as vendors, budget, guests, seating, RSVPs, registry, gift tracking, inquiries, and website content without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires handling a long-lived Zola refresh token that can provide direct account access.

Mitigation: Treat the token like a password and keep it out of chats, logs, shared terminals, shell history, and committed files.

Risk: Ready-to-run commands can change or delete live wedding data, including guest PII, registry, budget, invitations, website content, and settings.

Mitigation: Manually review every write or delete payload before execution and prefer read-modify-write flows that preserve existing fields.

Risk: Raw non-2xx API error bodies may include sensitive session details.

Mitigation: Do not paste raw API error responses into public or shared locations without first checking for secrets.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [Zola website](https://www.zola.com)
- [Zola mobile API](https://mobile-api.zola.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return live Zola account data and can perform write or delete operations when executed.]

## Skill Version(s):

1.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
