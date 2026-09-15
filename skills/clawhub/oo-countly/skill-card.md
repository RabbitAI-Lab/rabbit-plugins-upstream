## Description:

Countly (countly.com) skill for searching and reading Countly application, dashboard, event, session, and user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to inspect Countly applications and retrieve read-only Countly analytics through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Use an already installed oo CLI when possible, or install through a reviewed, pinned, or package-manager path before running connector actions.

Risk: Connector actions depend on a connected OOMOL account and Countly API-key configuration.

Mitigation: Run only read actions after authentication succeeds, and use the documented setup path only when an auth or connection error occurs.

## Reference(s):

- [Countly homepage](https://countly.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-countly)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Skill icon](https://static.oomol.com/logo/third-party/countly.svg)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses from the oo CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
