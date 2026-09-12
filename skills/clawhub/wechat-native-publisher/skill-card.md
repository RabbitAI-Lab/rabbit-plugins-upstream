## Description:

Renders finalized text, Markdown, or preformatted HTML into WeChat-native rich text and can create WeChat public-account drafts with themes, previews, cover generation, and pre-publish checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, editors, writers, and developers use this skill to convert finished articles into WeChat-compatible rich text, preview the result, generate covers, and push drafts to a public account draft box.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use WeChat public-account draft API credentials and article assets.

Mitigation: Use a dedicated credential file via --config, keep secrets outside the skill directory, and limit access to the account and assets needed for draft creation.

Risk: The --build path executes user-selected Python article modules.

Mitigation: Use --build only with trusted modules that you have reviewed.

Risk: Skipping validation or forcing blocked output can bypass pre-publish checks.

Mitigation: Avoid --no-validate and --force unless the rendered output has been manually reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/wechat-native-publisher)
- [WeChat rich-text whitelist reference](artifact/references/wechat-whitelist.md)

## Skill Output:

**Output Type(s):** [text, markdown, HTML, files, shell commands, configuration, guidance]

**Output Format:** [Markdown or text inputs converted to WeChat-compatible HTML/rich text, optional preview files, cover images, and draft-creation commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call WeChat public-account APIs when pushing drafts; preview mode can run locally without creating a draft.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter lists 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
