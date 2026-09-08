## Description:

Renders finalized plain text, Markdown, or preformatted HTML into WeChat-compatible rich text and can push it to a WeChat official account draft box.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, editors, writers, and developers use this skill to convert finalized articles into WeChat-native rich text, preview the rendered layout, generate covers, validate formatting, and create WeChat official account drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles WeChat account credentials and can create account drafts.

Mitigation: Install only when the publisher and article inputs are trusted, keep config.json outside the skill directory, and review the WeChat draft before any publication step.

Risk: Validation and publishing controls can be bypassed with override flags.

Mitigation: Avoid --no-validate and --force except for trusted content that has been independently reviewed.

Risk: The component module workflow can execute user-provided Python modules.

Mitigation: Do not run --build on modules from untrusted sources.

Risk: Credential-related status output may appear in shared logs.

Mitigation: Avoid running the credential checks in shared logs until token-prefix logging is removed.

## Reference(s):

- [WeChat rich text whitelist](references/wechat-whitelist.md)
- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/wechat-native-publisher)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; bundled scripts can produce HTML previews, cover images, JSON profile configuration, and WeChat draft submissions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided WeChat account credentials for draft publishing; local preview mode can be used without publishing.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
