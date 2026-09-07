## Description:

Checks product listing images against machine-checkable marketplace requirements, reports rejection risks, and can create geometry and color fixes for supported platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketplace operators, and ecommerce content teams use this skill to check product images before listing them on Amazon, TikTok Shop, Temu, Shopee, Shopify, or Taobao. It helps identify objective image-specification failures and can propose or run local fixes for white backgrounds, occupancy, resolution, file size, and format issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes optional cloud-generation provider code that can send prompts, referenced local images, and API credentials outside the local compliance-check workflow.

Mitigation: Use the local check_listing.py workflow for compliance checks, review the selected provider before running generation code, avoid untrusted ARK_BASE_URL values, and assume images or prompts may be uploaded when cloud providers are used.

Risk: Pixel-level checks cannot determine whether an image contains text, watermarks, collages, or product defects.

Mitigation: Route those content checks to a visual review workflow or human reviewer before publishing marketplace images.

Risk: Marketplace image rules can change, so built-in thresholds may become stale.

Mitigation: Confirm current platform requirements and override built-in rules with a custom rules JSON when a marketplace policy differs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline bash commands; optional JSON compliance reports and fixed image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local checks use Pillow and exit codes; optional provider workflows may require API credentials]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
