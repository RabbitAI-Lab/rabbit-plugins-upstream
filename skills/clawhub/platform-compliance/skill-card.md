## Description:

Checks product listing images against marketplace image requirements and can correct common background, sizing, and layout issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Online sellers and developers check product images before publishing to Amazon, TikTok Shop, Temu, Shopee, Shopify, or Taobao. They can inspect rule-by-rule rejection risks and optionally save corrected images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled generation tools can send prompts and images to external AI providers, beyond local compliance checking.

Mitigation: Use the local image checker for compliance checks; avoid generation and provider tools unless external data transfer and credentials are explicitly approved.

Risk: Automatic image corrections may crop content or leave visual issues that pixel checks cannot detect.

Mitigation: Review changes before fixing, then inspect corrected images and check text, watermarks, and product quality manually.

Risk: Built-in marketplace thresholds may not reflect current listing requirements.

Mitigation: Compare against the destination platform's current rules and supply updated custom rules where necessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files]

**Output Format:** [Plain-text or JSON compliance reports; optional corrected JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports measurements and rule outcomes; image fixes are saved separately and rechecked. Pixel-based checks do not detect text, watermarks, or product defects.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
