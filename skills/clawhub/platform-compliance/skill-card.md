## Description:

Checks product listing images before publication against machine-checkable marketplace rules, reports rejection risk, and can create corrected image files for objective geometry, background, resolution, and file-size issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, developers, and agents use this skill to check product images before submitting them to marketplaces such as Amazon, TikTok Shop, Temu, Shopee, Shopify, and Taobao. It supports local compliance reports and optional automated fixes for measurable image constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes optional cloud generation utilities that can upload prompts and local images to external providers.

Mitigation: For local-only compliance checking, run scripts/check_listing.py, avoid scripts/gen.mjs, do not configure provider API keys for this skill, and do not pass sensitive or proprietary images to generation providers unless upload is intended.

Risk: Marketplace image rules can change after the bundled machine-checkable thresholds are published.

Mitigation: Verify current marketplace documentation for the target listing path and use --rules with a custom rule file when platform requirements differ.

## Reference(s):

- [Platform image specification reference](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/platform-compliance)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [Console report or JSON, with optional corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes distinguish pass, rejection risk, and input or read errors.]

## Skill Version(s):

1.0.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
