## Description:

Query or update Zola wedding-planning data through its mobile API using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Zola account holders can use the skill to retrieve or update vendors, budgets, guests, seating, RSVPs, registry data, and wedding website content from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can expose a reusable login token, and update examples could cause unintended privacy or data changes.

Mitigation: Load the token privately, redact credential-bearing output, and replace any token exposed in accessible logs. Review updates to search visibility and RSVP questions, and preserve existing fields when applying changes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/zola-api)
- [Mobile API endpoint recipes](references/mobile-api-endpoints.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON API data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve or modify Zola wedding account data.]

## Skill Version(s):

2.1.12 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
