## Description:

ConfigCat lets an agent read ConfigCat products, configs, environments, settings, and setting values through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect ConfigCat feature flag data from an OOMOL-connected account without handling raw ConfigCat tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that run shell code from an online delivery path.

Mitigation: Review the installer source and prefer official, versioned, integrity-verified oo CLI installation instructions before running setup commands.

Risk: Connector results depend on the authenticated OOMOL account and the active ConfigCat connection state.

Mitigation: Inspect the live action schema before each connector request and confirm exact targets before any future write or destructive action is used.

## Reference(s):

- [ConfigCat homepage](https://configcat.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash and PowerShell command examples plus JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId; live action schemas should be inspected before execution.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
