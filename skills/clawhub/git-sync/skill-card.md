## Description:

Automates cross-platform publishing for skills and agents, including Gitee/GitHub sync, ClawHub/SkillHub/PyPI publishing, release creation, LLM-assisted file filtering, and sensitive-data sanitization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ldxs001](https://clawhub.ai/user/ldxs001)

### License/Terms of Use:

MIT

## Use Case:

Developers and release maintainers use git-sync to package, synchronize, publish, and create releases for skill or agent projects across Git, ClawHub, SkillHub, and PyPI. It is best suited for intentional release automation where repository, credential, and publishing side effects are expected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can push to repositories and publish releases or packages using configured credentials.

Mitigation: Install only for intentional release automation, use least-privilege tokens, and require explicit confirmation before push, publish, release, or all-mode operations.

Risk: Credential handling may read or reuse stored Git credentials and can expose tokens through command arguments or remote URL handling.

Mitigation: Review and patch credential handling before use: avoid global credential.helper=store, avoid automatic reuse of ~/.git-credentials, and avoid passing tokens in command arguments.

Risk: File filtering and sensitive-data sanitization depend on follow-up decision files during an automated workflow.

Mitigation: Review allowed files and sanitization choices before publishing, and keep the documented single-command rerun flow so decisions are applied to the intended run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/git-sync)
- [Publisher profile](https://clawhub.ai/user/ldxs001)
- [Guide](references/guide.md)
- [Command reference](references/reference.md)
- [Permissions and security notes](references/permissions.md)
- [License](references/LICENSE.md)
- [PyPI Trusted Publishers documentation](https://docs.pypi.org/trusted-publishers/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON decision files, and release/publish status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write release artifacts, update repository files, invoke publishing CLIs, and require follow-up JSON decisions for file filtering or sanitization.]

## Skill Version(s):

2.45.8 (source: SKILL.md frontmatter, _meta.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
