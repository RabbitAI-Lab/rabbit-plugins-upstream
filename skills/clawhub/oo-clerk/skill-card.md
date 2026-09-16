## Description:

Clerk helps an agent manage Clerk users through OOMOL's oo CLI connector, including account reads, filtering, creation, updates, locks, bans, and deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Clerk user accounts from an agent, using live action schemas before requests and explicit confirmation for write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path uses remote installer commands that can execute code on the user's machine.

Mitigation: Install only through a trusted OOMOL CLI distribution path and manually review or verify the installer before running it.

Risk: Write and destructive Clerk actions can change, ban, lock, or delete user accounts.

Mitigation: Require explicit user confirmation of the target, payload, and intended effect before running any write, ban, lock, or delete action.

Risk: The skill depends on connecting Clerk through OOMOL.

Mitigation: Use it only when the user is comfortable authorizing Clerk through OOMOL and has connected the account with appropriate scopes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clerk)
- [Clerk homepage](https://clerk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Clerk connector action schemas and returns connector JSON responses when commands are run.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
