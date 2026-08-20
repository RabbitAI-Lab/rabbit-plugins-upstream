## Description:

git-sync automates release publishing for skills and agents across Gitee, GitHub, ClawHub, SkillHub, and PyPI, including release creation, LLM-assisted file filtering, and sensitive-data sanitization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ldxs001](https://clawhub.ai/user/ldxs001)

### License/Terms of Use:

MIT

## Use Case:

Developers and release engineers use this skill to synchronize, package, scan, and publish skill or agent projects to configured repositories, marketplaces, package indexes, and release channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports persistent host-wide Git credential changes and local credential handling.

Mitigation: Install and run the skill only in a dedicated workspace or VM with scoped tokens and review credential configuration before use.

Risk: The security evidence notes automatic git push, marketplace publishing, PyPI publishing, and release creation behavior.

Mitigation: Review the selected mode and flags before execution, especially --skip-market, --market-only, --pypi, --release, and all-mode behavior.

Risk: The artifact describes file synchronization, file deletion, and mandatory sensitive-data sanitization steps.

Mitigation: Inspect configured source and destination paths, manifest entries, and sanitization decisions before publishing outputs externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/git-sync)
- [User guide](artifact/references/guide.md)
- [Command reference](artifact/references/reference.md)
- [Permissions and testing](artifact/references/permissions.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated repository, package, and release files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform repository writes, publishing actions, release creation, package uploads, and local credential handling when invoked with those modes.]

## Skill Version(s):

2.45.7 (source: frontmatter, _meta.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
