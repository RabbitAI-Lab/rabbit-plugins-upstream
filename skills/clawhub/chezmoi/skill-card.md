## Description:

chezmoi helps agents manage dotfile workflows, including diff-reviewed applies, template consolidation, cross-platform fixes, environment checks, and MCP configuration synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to inspect and apply chezmoi dotfile changes, consolidate reusable modify scripts, troubleshoot macOS and Windows compatibility, and synchronize MCP server configuration across local tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled SourceGit helper starts Claude with permission checks disabled and resumes a session against a supplied repository.

Mitigation: Install or invoke the helper only when that behavior is intended, review it before copying it into ~/bin, and avoid using it on untrusted repositories.

Risk: Dotfile and MCP synchronization workflows can move sensitive values into plain chezmoi-managed configuration files.

Mitigation: Keep secrets encrypted or in a separate secret store, and review generated configuration before applying changes.

Risk: Applying chezmoi changes without a visible diff can overwrite or misconfigure local application settings.

Mitigation: Run and show chezmoi diff before apply, skip empty diffs, and apply only after explicit user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/chezmoi)
- [Publisher profile](https://clawhub.ai/user/drumrobot)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON/TOML snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user review of diffs before applying dotfile changes.]

## Skill Version(s):

0.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
