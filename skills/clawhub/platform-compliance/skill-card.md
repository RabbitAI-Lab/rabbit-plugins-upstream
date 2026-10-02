## Description:

Checks product listing images against marketplace image specifications, reports rejection risks, and can produce corrected images for measurable format, background, and layout issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers, creative teams, and developers use this skill to check product images before listing on Amazon, TikTok Shop, Temu, Shopee, Shopify, or Taobao. It flags measurable image-specification issues and optionally saves revised images for another check.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled generation tools can transmit product images and prompts to external AI providers using local credentials.

Mitigation: For local-only checks, restrict execution to scripts/check_listing.py; use generation tools only when external transmission is intended and approved.

Risk: Pixel checks and automatic corrections cannot identify text, watermarks, or visibly defective products.

Mitigation: Review image content manually or with a separate visual inspection before publishing.

Risk: Marketplace requirements can change, so a passing report may not ensure listing acceptance.

Mitigation: Compare results with current marketplace requirements and update the custom rules when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files]

**Output Format:** [Plain-text or JSON compliance report; optional corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports individual checks and rejection risk; corrected images are saved separately from originals.]

## Skill Version(s):

1.0.15 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
