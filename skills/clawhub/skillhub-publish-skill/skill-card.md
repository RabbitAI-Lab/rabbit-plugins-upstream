## Description:

Packages and publishes local Skills to SkillHub and ClawHub with preflight checks, dry-run validation, status lookup, category guidance, and WAF rejection diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill to prepare, validate, publish, inspect, and troubleshoot SkillHub and ClawHub skill releases. It is especially useful when publication fails because of package shape, category metadata, version checks, or SkillHub WAF 566 rejections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, update, list, and delete marketplace content using an existing SkillHub account, and the security summary notes there is no enforced confirmation step for all publishing actions.

Mitigation: Run dry-run and preflight first, confirm the exact files, slug, version, host, and destination account before live publishing, and require explicit user confirmation before account-changing actions.

Risk: Using an untrusted host could send release data or account-backed requests to the wrong endpoint.

Mitigation: Avoid --host unless the target is the trusted SkillHub API endpoint.

Risk: The optional curl-to-bash installer can execute remote code.

Mitigation: Verify the installer source and contents before running it, or use a manual installation path.

## Reference(s):

- [SkillHub/ClawHub skill page](https://clawhub.ai/oracis/skills/skillhub-publish-skill)
- [SkillHub CLI publishing tutorial](https://skillhub.cn/tutorials#publish-via-cli)
- [ClawHub categories and topics](artifact/references/clawhub-catalog.md)
- [SkillHub categories and subcategories](artifact/references/categories.md)
- [SkillHub icon upload flow](artifact/references/icon-upload.md)
- [SkillHub WAF 566 diagnosis](artifact/references/waf-details.md)
- [CLI installation and browser fallback](artifact/references/cli-install.md)
- [Windows path and slug pitfalls](artifact/references/path-traps.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python script invocations, and structured validation output when scripts are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run publishing, preflight, status, category, cleanup, and WAF-diagnosis commands against local skill directories and marketplace endpoints.]

## Skill Version(s):

1.7.3 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
