## Description:

Find and fix leaked API keys, tokens and passwords in your AI agent's config, long/short-term memory and session transcripts (OpenClaw + Claude Code). Use when the user asks to check token or secret safety, scan for leaked credentials, audit agent memory, MEMORY.md, CLAUDE.md or chat history for secrets, move plaintext tokens in openclaw.json to env vars, or stop secrets from being written into memory. Also use after editing openclaw.json or when setting up a new OpenClaw instance. Secret values are never printed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maoisdamao](https://clawhub.ai/user/maoisdamao)

### License/Terms of Use:

MIT

## Use Case:

Developers using Claude Code or OpenClaw can scan configuration, memory, and transcripts for exposed credentials, get safe rotation guidance, and optionally migrate OpenClaw config secrets or enable write guards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential migration can leave passwords and tokens readable by other users.

Mitigation: Make the destination profile private before migrating, do not rely on --secure-profile to protect the initial write, and use exclusive private temporary files for migration and settings updates.

Risk: Persistent hooks affect future writes or commits on the selected platforms.

Mitigation: Review the selected platforms and scope before enabling hooks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maoisdamao/skills/token-safety-checker)
- [Publisher profile](https://clawhub.ai/user/maoisdamao)
- [Project homepage](https://github.com/maoisdamao/token-safety-checker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Text and Markdown scan summaries with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Secret values are not printed; findings use paths, line numbers, detector names, lengths, and fingerprints.]

## Skill Version(s):

3.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
