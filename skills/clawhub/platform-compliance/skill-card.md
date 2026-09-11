## Description:

Checks e-commerce listing images against machine-checkable platform rules for Amazon, TikTok Shop, Temu, Shopee, Shopify, and Taobao, reports rejection risks, and can create corrected image files for geometry and color compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, listing operators, and developers use this skill to check product images before publishing, identify platform rejection risks, and apply local fixes such as white-background, occupancy, resolution, format, and file-size adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled generation tooling can send prompts, selected images, and credentials to configured external providers.

Mitigation: For sensitive or unreleased product images, use the local compliance checker and avoid generation tooling unless provider data sharing is approved.

Risk: Provider endpoint or credential misconfiguration could expose images or secrets outside the intended service.

Mitigation: Use official provider endpoints only, do not set ARK_BASE_URL to a nonofficial endpoint, and review credential configuration before execution.

Risk: The compliance checker covers objective pixel and file properties, but it cannot determine text, watermark, collage, or product-quality issues.

Mitigation: Pair the checker with visual model review or manual review for content-level policies before publishing.

Risk: Marketplace image rules can change after the bundled rule set is released.

Mitigation: Confirm current platform requirements and override rules with a custom rules JSON when platform policy differs from the bundled thresholds.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown status reports, optional JSON reports, shell commands, and corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local checker returns exit code 0 for pass, 1 for rejection risk, and 2 for argument or image-read errors.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
