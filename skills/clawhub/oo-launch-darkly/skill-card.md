## Description:

Enables agents to inspect action schemas and operate LaunchDarkly resources through the OOMOL-connected oo CLI for read, write, search, and delete workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage LaunchDarkly projects, environments, feature flags, segments, members, teams, tokens, contexts, and tags from an agent while checking live action schemas before submitting payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer LaunchDarkly access tokens and other sensitive account resources.

Mitigation: Install only when the OOMOL publisher and granted LaunchDarkly connector scopes are trusted, and confirm exact targets and payloads before token, write, or destructive actions.

Risk: First-time setup documents pipe-to-shell installer commands.

Mitigation: Avoid running remote installer commands unless the installer source and integrity have been independently verified.

Risk: Write and destructive actions can change or remove LaunchDarkly state.

Mitigation: Inspect the live action schema before building payloads, require user confirmation for writes, and require explicit approval for destructive operations.

## Reference(s):

- [ClawHub LaunchDarkly Skill Page](https://clawhub.ai/oomol/skills/oo-launch-darkly)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [LaunchDarkly Homepage](https://launchdarkly.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require confirmation and destructive actions require explicit approval before execution.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
