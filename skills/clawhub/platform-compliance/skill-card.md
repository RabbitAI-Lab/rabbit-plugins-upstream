## Description:

Checks product listing images against platform image specifications and can automatically correct measurable format, background, and layout issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and developers check product photos before listing on Amazon, TikTok Shop, Temu, Shopee, Shopify, or Taobao, then optionally create corrected image files for measurable failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional generation workflows can upload product images and prompts to cloud providers.

Mitigation: Use the local compliance checker for private images; only invoke generation providers when sharing the assets and prompts is acceptable.

Risk: A passing pixel-level check may miss watermarks, text, or other content violations, and platform rules can change.

Mitigation: Review image content manually and confirm current platform requirements before publishing; update custom rules as needed.

Risk: Automatic resizing or cropping may change the product composition without fixing image quality.

Mitigation: Inspect corrected images and rerun the check before listing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Optional provider workflows](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Image files]

**Output Format:** [Plain-text or JSON compliance report; optional corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports measured checks and rejection risks; optional fixes save separately from source images.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
