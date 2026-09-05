## Description:

Checks and optionally fixes product listing images against platform-specific requirements for Amazon, TikTok Shop, Temu, Shopee, Shopify, and Taobao.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers, e-commerce operators, and agents use this skill to evaluate listing images before upload, identify objective rejection risks, and apply geometry or color fixes when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes generation and provider tooling that can send prompts and images to third-party cloud services.

Mitigation: Use the local check_listing.py workflow for image compliance checks, and run remote provider modes only when third-party upload of the input images is approved.

Risk: Automated fixes address geometry and color compliance, but they do not detect or remove watermarks, text overlays, product defects, or other content problems.

Mitigation: Review content manually or pair this skill with an appropriate visual review workflow before publishing images.

Risk: Marketplace image requirements can change after the bundled rule set is released.

Mitigation: Confirm current platform requirements before relying on a pass result, or provide updated custom rules through the supported rules file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown or text compliance reports, optional JSON reports, and fixed JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local checker returns process exit codes for automation and can write repaired images to a caller-specified output directory.]

## Skill Version(s):

1.0.3 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
