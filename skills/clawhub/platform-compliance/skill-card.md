## Description:

Checks product listing images against marketplace image rules, reports rejection risks, and can fix measurable image-specification issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and ecommerce teams check listing images against Amazon, TikTok Shop, Temu, Shopee, Shopify, or Taobao requirements before upload, and optionally correct measurable image issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled generation tools can send prompts and product images to external providers beyond local compliance checking.

Mitigation: For local checks, run only the compliance checker. Review provider destinations, approve any sensitive-image upload, and manage API keys deliberately before using generation tools.

Risk: Pixel-based checks cannot identify watermarks, text, or damaged products; automatic fixes can alter framing.

Mitigation: Review content and proposed framing changes manually, then recheck corrected images against the intended marketplace rules.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications](references/platform-specs.md)
- [Optional provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files, Guidance]

**Output Format:** [Human-readable compliance report or structured JSON; optional corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports measured checks and rejection risks; optional fixes address geometry and color, not image content.]

## Skill Version(s):

1.0.21 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
