## Description:

Polish any GitHub repository's surface — labels (emoji rating tiers, P0–P3 priority, impact severity), issue forms, PR template, CI workflows, CODEOWNERS, rulesets, docs. Repo meta & config only — no code logic touched. Use when creating a new repo or polishing an existing one.

This skill is ready for commercial/non-commercial use.

## Publisher:

[programmingwtf](https://clawhub.ai/user/programmingwtf)

### License/Terms of Use:

MIT

## Use Case:

Developers and maintainers use this skill to standardize GitHub repository metadata and configuration, including labels, issue forms, pull request templates, CI workflows, CODEOWNERS, branch rulesets, and project documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make meaningful repository metadata and configuration changes, including CI workflow files, labels, and branch rulesets.

Mitigation: Review the dry-run plan carefully before allowing changes, especially for private or organization repositories and settings used by automation.

Risk: Repository access depends on the active GitHub CLI account and token scopes.

Mitigation: Confirm the acting account and required scopes before changes, and avoid sharing tokens in chat, logs, or files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/programmingwtf/skills/repo-standardizer)
- [Architecture](docs/ARCHITECTURE.md)
- [README](README.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and generated repository configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a dry-run plan and verification checklist before or after applying repository metadata and configuration changes.]

## Skill Version(s):

0.2.7 (source: server release metadata and changelog, released 2026-08-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
