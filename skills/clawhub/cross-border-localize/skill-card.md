## Description:

跨境一套素材多区域本地化：将一套电商素材转成多语言文案、尺码换算表、区域主图和常见合规标识提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and listing teams use this skill to adapt product assets for cross-border marketplaces by planning localized copy, size conversion, regional image variants, and pre-publish listing checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts, images, and brand guidance may be sent to the selected cloud generation provider.

Mitigation: Use dry-run or doctor mode before generation, choose the provider intentionally, and avoid confidential unreleased assets unless approved.

Risk: Generated localized text, especially non-English text embedded in images, may contain errors.

Mitigation: Review generated text before publishing; for important non-English text, use a native-speaker review or generate text-free images and add copy in post-production.

Risk: Compliance labels and marketplace checks are prompts and machine-checkable subsets, not legal advice or complete platform policy coverage.

Mitigation: Confirm regional compliance requirements through qualified channels and verify final listings against the current marketplace rules before release.

## Reference(s):

- [平台图片规格（可机检子集）](references/platform-specs.md)
- [后端调用参考](references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/cross-border-localize)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with shell command examples and generated image file paths or JSON status when scripts are run with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce localized listing recommendations, size table guidance, image generation prompts, saved ecommerce image files, and platform compliance check results.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
