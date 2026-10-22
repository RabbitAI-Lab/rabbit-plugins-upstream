## Description:

Installs an optional, fully local MCP and CLI bus that lets compatible CAD skills share project state and drawing-analysis contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers managing CAD and quantity-takeoff workflows use this installer to enable compatible skills to reuse local project state and drawing-analysis contracts. If the bus is unavailable, connected skills can fall back to their own local state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may register the MCP server in Codex configuration.

Mitigation: Preview with --dry-run; use SKIP_MCP_REG=1 to copy files without registering MCP.

Risk: Shared CAD state and configuration backups may contain sensitive project information.

Mitigation: Protect the local shared state and configuration backups.

Risk: Uninstalling removes MCP registration but leaves installed files and saved project data.

Mitigation: Remove remaining files and project data separately if a full cleanup is intended.

Risk: Integration wrappers rely on separately installed CAD skills.

Mitigation: Review the separately installed CAD skills used by the wrappers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/lis-skill-bus)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON project-state records, CLI commands, and MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores project state locally and supports CLI use or optional stdio MCP registration.]

## Skill Version(s):

0.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
