## Description:

Getnote Openclaw connects an agent to the official GetNote CLI so users can authenticate, diagnose connectivity, upgrade the CLI on request, and save, search, read, organize, share, and manage notes in their real GetNote account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill to let an agent operate the official GetNote CLI for user-directed note capture, search, reading, organization, tag management, sharing, deletion, authentication, diagnostics, and CLI updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on a user's real GetNote account and read or modify notes, folders, tags, shares, and subscriptions through the official CLI.

Mitigation: Install only for users who want this account access; require clear user intent and confirmation before deletes, public shares, folder removals, tag replacement, or other destructive or public operations.

Risk: Authentication and diagnostics involve local browser authorization and credential state managed by the CLI.

Mitigation: Use browser-based authorization only, do not ask for API keys, cookies, or Authorization headers, and avoid displaying full credentials in responses.

Risk: Asynchronous saves, uncertain writes, or failed CLI calls can lead to false success reports or duplicate changes.

Mitigation: Check exit code and JSON success fields, poll task status when needed, verify server state after writes, and avoid blind retries after uncertain write outcomes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iswalle/skills/getnote)
- [ClawHub publisher profile](https://clawhub.ai/user/iswalle)
- [Authentication, diagnosis, and CLI updates](references/auth.md)
- [Note operations](references/note.md)
- [Search](references/search.md)
- [Knowledge bases and folders](references/kb.md)
- [Tags](references/tag.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with CLI command execution guidance and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include real note titles, string IDs, links, status summaries, error details, and request IDs returned by the GetNote CLI.]

## Skill Version(s):

2.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
