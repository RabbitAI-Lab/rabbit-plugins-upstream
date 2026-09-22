## Description:

Checks ecommerce listing images against platform-specific objective requirements and can produce fixed images for geometry, background, resolution, and file-size compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, operators, and developers use this skill to check product images before listing them on marketplaces such as Amazon, TikTok Shop, Temu, Shopee, Shopify, and Taobao. It identifies objective rejection risks and can create corrected image files for supported geometric and color issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes generation and provider scripts that exceed the local compliance-checking purpose and may send prompts or images to external services when invoked with configured credentials.

Mitigation: For compliance-only use, run scripts/check_listing.py and avoid invoking gen.mjs or configuring provider API keys unless external generation is intended.

Risk: Pixel-level checks cannot determine whether an image contains text, watermarks, collage elements, product defects, or marketplace rules that changed after the bundled thresholds were written.

Mitigation: Pair the report with visual or human review for content issues and override platform thresholds with --rules when current official requirements differ.

Risk: Automatic fixes only adjust geometry, background, resolution, and file size; they do not repair image quality, remove watermarks, or correct product defects.

Mitigation: Review fixed outputs before upload and route content or quality defects to the appropriate repair workflow.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/platform-compliance)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance, files]

**Output Format:** [Plain text compliance report, optional JSON report, and optional corrected JPEG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The checker exits 0 when inputs pass and 1 when rejection risk remains; --fix writes corrected files to a separate output directory.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
