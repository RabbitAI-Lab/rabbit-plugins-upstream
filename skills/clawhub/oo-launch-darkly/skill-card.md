## Description:

LaunchDarkly enables agents to read, create, update, and delete LaunchDarkly resources through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to administer LaunchDarkly projects, environments, feature flags, segments, teams, members, contexts, tags, and tokens through an agent using an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute unverified code.

Mitigation: Do not allow an agent to run the installer automatically; install the oo CLI through a verified or package-managed method where possible.

Risk: Write, delete, reset, and token actions can make administrative changes to LaunchDarkly resources.

Mitigation: Require explicit user review of the action, target, and payload before executing write or destructive operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-launch-darkly)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [LaunchDarkly](https://launchdarkly.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run.]

## Skill Version(s):

1.0.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
