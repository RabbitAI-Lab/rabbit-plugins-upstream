## Description:

Helps agents choose and inventory YottaMeta skills, install or update them, and manage a shared local skill hub across agent hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to identify suitable YottaMeta skill combinations, inspect installed skills, and manage installations and links across local agent hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and hub operations can download packages, write skill directories, and move or remove managed copies across agent hosts.

Mitigation: Review target directories and planned changes with dry-run and status commands; prefer version-pinned installations and confirm each write operation before running it.

Risk: Some documented confirmation protections are not enforced by the CLI itself, and bypass flags can weaken safeguards.

Mitigation: Require an independent review before executing CLI write commands; avoid --force, --skip-scan, and --allow-unverified unless their effects are understood.

Risk: Optional provider features may use local provider configuration.

Mitigation: Review ~/.yottameta/provider.json before enabling provider features.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-skills)
- [Skill orchestration guide](references/orchestration.md)
- [Skill hub guide](references/hub.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with commands and installation status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional JSON output for inventory and status commands.]

## Skill Version(s):

0.29.10 (source: server release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
