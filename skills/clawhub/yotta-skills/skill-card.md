## Description:

Helps agents plan and route YottaMeta skill combinations, inspect installed skills, and preview or perform user-approved installation and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to choose complementary YottaMeta skills, review installation plans, install or update approved skills, and inventory local skill directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating skills can download packages and change local agent skill directories.

Mitigation: Review the target directory and --dry-run plan, obtain user approval, and pin the package version in sensitive environments.

Risk: Automatic updates, skipped scans, optional providers, or changes to global memory and MCP settings can broaden access or alter agent behavior.

Mitigation: Enable --auto, --skip-scan, providers, --global, memory writes, or MCP configuration only after explicit review of their scope; prefer native install/update where available.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage (listed in Clawdis metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-skills)
- [Orchestration guide](artifact/references/orchestration.md)
- [Installation guide](artifact/references/install-flow.md)
- [Provider protocol](artifact/references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance or structured CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routing suggestions include candidate skills and install commands; inventory and route results can be machine-readable.]

## Skill Version(s):

0.20.0 (source: server release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
