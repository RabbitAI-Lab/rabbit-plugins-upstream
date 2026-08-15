## Description:

Polish any GitHub repository's surface — labels (emoji rating tiers, P0–P3 priority, impact severity), issue forms, PR template, CI workflows, CODEOWNERS, rulesets, docs. Repo meta & config only — no code logic touched. Use when creating a new repo or polishing an existing one.

This skill is ready for commercial/non-commercial use.

## Publisher:

[programmingwtf](https://clawhub.ai/user/programmingwtf)

### License/Terms of Use:

MIT

## Use Case:

Developers, maintainers, and repository administrators use this skill to standardize GitHub repository metadata and configuration, including labels, issue forms, pull request templates, CI workflows, CODEOWNERS, branch rulesets, and docs. It is intended for creating a professional baseline on new repositories or reconciling drift on existing repositories without changing source code logic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer GitHub repository metadata and configuration on the selected repository.

Mitigation: Specify the exact OWNER/REPO and desired modules before use, then review the dry-run plan before approving changes.

Risk: CI workflow, CODEOWNERS, AI-guide, label deletion, branch protection, and ruleset changes can affect repository governance or automation behavior.

Mitigation: Require explicit confirmation for sensitive modules and inspect diffs or planned API changes before applying them.

Risk: Authenticated GitHub CLI access may require repository, workflow, or organization privileges.

Mitigation: Use the least-privileged account or token that can complete the requested task, confirm the acting account, and never expose tokens in chat, logs, or files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/programmingwtf/skills/repo-standardizer)
- [Architecture](docs/ARCHITECTURE.md)
- [README](README.md)
- [Security policy](SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, GitHub API calls, YAML/JSON configuration, and repository file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the GitHub CLI and git; selected modules may also use jq and python3 for label processing.]

## Skill Version(s):

0.2.7 (source: server release evidence and CHANGELOG, released 2026-08-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
