## Description:

git-sync automates skill and agent synchronization, packaging, marketplace publishing, PyPI publishing, and release creation across configured Git and marketplace targets, with LLM-assisted file filtering and mandatory sensitive-data sanitization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ldxs001](https://clawhub.ai/user/ldxs001)

### License/Terms of Use:

MIT

## Use Case:

Developers and release maintainers use git-sync to prepare, sanitize, package, and publish ClawHub skills or agents across configured repositories and marketplaces. It is intended for explicit sync, package, publish, upload, or release workflows rather than general-purpose Git commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary marks this release suspicious because execution can change global Git credential helper settings, read stored credentials, push to configured remotes, and publish code.

Mitigation: Review before installing; run only with repositories and source trees you trust, use scoped tokens or a test account, and verify target remotes and safer flags before execution.

Risk: Publishing and sync workflows can propagate unintended files or sensitive data if the target project, configuration, or decision files are wrong.

Mitigation: Use the documented file-filter and mandatory sanitization checkpoints, inspect generated decisions and package contents, and confirm repository and marketplace targets before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/git-sync)
- [Guide](references/guide.md)
- [Command reference](references/reference.md)
- [Permissions report](references/permissions.md)
- [Changelog](references/changelog.md)
- [License](references/LICENSE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown and terminal text with generated files, JSON decision files, shell command invocations, and release or publishing status messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update repository files, README content, ZIP packages, release tags, marketplace submissions, and sync manifests depending on selected flags.]

## Skill Version(s):

2.45.4 (source: SKILL.md frontmatter, _meta.json, release metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
