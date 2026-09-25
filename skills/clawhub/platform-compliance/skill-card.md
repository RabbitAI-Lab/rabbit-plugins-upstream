## Description:

Checks marketplace listing images before publication and reports or fixes objective rejection risks for platforms such as Amazon, TikTok Shop, Temu, Shopee, Shopify, and Taobao.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and ecommerce automation agents use this skill to check product images against platform-specific, machine-testable listing requirements and optionally generate corrected files. It is focused on objective image properties such as background color, size, format, transparency, borders, and subject occupancy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes generation utilities that can send prompts and images to external services if invoked.

Mitigation: For the advertised compliance-checking purpose, use scripts/check_listing.py locally and avoid invoking gen.mjs or configuring provider API keys unless external processing is intended.

Risk: Pixel-level checks cannot determine whether an image contains text, watermarks, collages, or product defects.

Mitigation: Use the checker output as an objective-specification screen and send manual or vision-model-only checks through a separate review step for content issues.

Risk: Marketplace image rules can change after the packaged thresholds were created.

Mitigation: Confirm current platform requirements for production listings and use a custom rules JSON file when the platform policy differs from the bundled machine-testable subset.

## Reference(s):

- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, text reports, and optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local checker can return pass, warning, rejection-risk, or error results and can write fixed JPEG files when invoked with the fix option.]

## Skill Version(s):

1.0.12 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
