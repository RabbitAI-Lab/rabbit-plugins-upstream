## Description:

Fly.io requests, including reading, creating, and updating Fly.io resources through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Fly.io connector schemas, run Fly.io actions through an OOMOL-connected account, and manage Fly Apps and Machines without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Replace those commands with a verified download or package-manager install, or inspect and pin the installer before execution.

Risk: The skill can perform state-changing Fly.io operations such as creating, starting, stopping, and restarting Machines.

Mitigation: Require user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

Risk: Actions operate through an OOMOL-connected Fly.io account and may affect live resources.

Mitigation: Use least-privilege Fly.io credentials, verify the connected account and organization before writes, and treat billing or connection errors as setup issues to resolve explicitly.

## Reference(s):

- [Fly.io homepage](https://fly.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fly)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, PowerShell commands, text links, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect live action schemas before constructing JSON payloads and to read JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
