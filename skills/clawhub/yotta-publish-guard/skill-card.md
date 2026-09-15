## Description:

元守 yotta-publish-guard helps agents and developers run pre-publish checks, package, version, and name validation, and dry-run-first publish command plans for skill releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and release agents use this skill before publishing skills to verify required files, version alignment, package contents, name availability, and generated publish commands. It supports GitHub-only, self-use, and multi-channel release checks while leaving final publishing decisions to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the publish execution path can run high-impact external commands and has an artifact-backed Windows command-injection risk.

Mitigation: Prefer dry-run mode, manually review generated commands, and avoid using --exec on Windows until command-argument validation is fixed.

Risk: When --exec is used, local npm, gh, and clawhub tools can publish through the user's existing authenticated CLI sessions.

Mitigation: Run execution only after confirming the target channels, owner handle, package name, and active CLI identities; keep credentials managed by the platform CLIs.

Risk: Network or DNS failures can leave npm, GitHub, or ClawHub name availability unconfirmed.

Mitigation: Treat unknown name-check results as requiring manual verification before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-publish-guard)
- [README](README.md)
- [Validation item details](references/check-items.md)
- [Three-channel publishing flow](references/publish-flow.md)
- [FAQ](references/faq.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run output is the default for publish plans; command execution requires explicit user selection.]

## Skill Version(s):

0.4.1 (source: SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
