## Description:

Query or update Zola wedding-planning data from a shell with curl against mobile-api.zola.com, covering vendors, budget, guests, seating, events and RSVPs, registry, gift tracker, inquiries, and wedding website data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and change Zola wedding-planning records through direct mobile API calls when the MCP server is unavailable or unnecessary. It is suited to scripted workflows that need curl and jq examples for authenticated Zola account data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a long-lived Zola refresh token and mints session tokens for live API access.

Mitigation: Treat the refresh token like a password, keep it out of shared terminals and logs, and install only where shell-level access to the Zola account is acceptable.

Risk: The skill includes commands that add, update, hide, unbook, remove, or delete wedding-planning data.

Mitigation: Require explicit confirmation before running mutating commands and review the exact account, registry, wedding, guest, event, or page identifiers before execution.

Risk: Several Zola write endpoints replace full objects, so partial bodies can erase unrelated fields.

Mitigation: Follow the documented read-modify-write recipes and preserve existing fields such as event invitations, colors, and full record bodies when changing individual values.

Risk: Non-2xx error bodies may expose sensitive session details if copied into public channels.

Mitigation: Inspect API errors locally and redact tokens or account-specific data before sharing logs or troubleshooting output.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [ClawHub zola-api skill page](https://clawhub.ai/chrischall/skills/zola-api)
- [Zola mobile API host](https://mobile-api.zola.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline curl and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate on live Zola account data and may return JSON API responses.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
