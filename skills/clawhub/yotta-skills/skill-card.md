## Description:

Helps developers plan and route skill combinations, inspect installed skills, and install or distribute YottaMeta skills across agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose skill combinations, inspect local installations, and manage installation, updates, and links across agent skill directories with explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and Hub linking can change multiple agent skill directories and local registries; documented boundaries are not fully consistent.

Mitigation: Use dry-run and explicit --dir or --agent targets, review affected paths, and confirm changes before installing or linking.

Risk: Downloaded packages and optional provider configuration can introduce unreviewed behavior.

Mitigation: Prefer pinned package versions and review any provider.json before use; avoid install.sh -g unless broad installation is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage (listed in release metadata)](https://github.com/YottaMeta/yotta-skills)
- [Hub usage guide](references/hub.md)
- [Installation workflow](references/install-flow.md)
- [Provider protocol](references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands; optional structured CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can recommend skill combinations and report inventory, installation, and link status.]

## Skill Version(s):

0.25.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
