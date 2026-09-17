## Description:

Browserbase helps agents operate Browserbase projects, sessions, usage, and contexts through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with OOMOL-connected Browserbase accounts use this skill to inspect live connector schemas and run Browserbase project, session, usage, and context actions. It supports read operations directly while requiring confirmation for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could run unreviewed code on the user's machine.

Mitigation: Install the oo CLI through a verifiable method and review installer sources before execution.

Risk: Write and destructive Browserbase actions can create, release, delete, or otherwise change account resources.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running create, release, delete, or credential-refresh actions.

Risk: The skill depends on an OOMOL-connected Browserbase account and can fail or behave unexpectedly when authentication, scopes, billing, or app connection state are missing.

Mitigation: Use it only with an intended OOMOL-connected Browserbase account and follow setup or billing remediation only after an action fails for that specific reason.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-browserbase)
- [Browserbase homepage](https://www.browserbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload or response references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes action names, setup fallback guidance, and confirmation requirements for write or destructive operations.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
