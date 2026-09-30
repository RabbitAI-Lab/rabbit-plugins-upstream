## Description:

Helps agents query and update Zola wedding-planning data directly from a shell using the Zola mobile API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Zola account holders and their agents can inspect or update wedding-planning information, including guests, events, budget, registry, and website content, through shell commands without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived refresh tokens and session tokens can grant direct access to a Zola account if exposed.

Mitigation: Treat tokens as passwords; do not paste them into chats or logs, and restrict access to the environment where commands run.

Risk: Live write or delete commands can change guests, registry, budget, events, website content, or invitations.

Mitigation: Preview the target and proposed change, and require explicit confirmation before executing each write or delete.

Risk: Some write endpoints replace whole records, potentially removing unrelated fields.

Mitigation: Read the current record first and preserve unchanged fields in the submitted update.

## Reference(s):

- [ClawHub zola-api release](https://clawhub.ai/chrischall/skills/zola-api)
- [Mobile API endpoint recipes](references/mobile-api-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and Markdown with curl and jq commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change live Zola account data.]

## Skill Version(s):

2.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
