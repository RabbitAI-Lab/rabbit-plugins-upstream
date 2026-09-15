## Description:

Drata lets agents retrieve and list Drata company, control, personnel, vendor, and workspace data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Drata compliance data, including company metadata, controls, personnel, vendors, and workspaces, from a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes one-line remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, versioned, verified method and do not let an agent run installer scripts automatically.

Risk: The skill can read Drata business and personnel data visible to the connected account.

Mitigation: Use least-privileged Drata and OOMOL credentials and review requested get or list actions before execution.

## Reference(s):

- [Drata homepage](https://drata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-drata)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run with --json.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
