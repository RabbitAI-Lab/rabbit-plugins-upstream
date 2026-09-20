## Description:

Use this skill for Assured Platform requests that search and read data through the OOMOL `assured_platform` connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect authenticated Assured Platform user and task data through an OOMOL-connected account. It fetches live connector schemas before execution and supports reading current user details, task details, and filtered task lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can pipe a remote oo CLI installer script directly into the shell.

Mitigation: Review the installer or install the CLI from a trusted, verified source, and run setup commands only after intentionally approving host-level changes.

Risk: The skill operates through an OOMOL-connected Assured Platform account and depends on that account's connection scopes and billing state.

Mitigation: Confirm the account connection, required scopes, and billing status before retrying failed connector calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-assured-platform)
- [Assured Platform homepage](https://www.withassured.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Assured Platform connection](https://console.oomol.com/app-connections?provider=assured_platform)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; read-only actions are safe to run directly, while any future write or destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: evidence release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
