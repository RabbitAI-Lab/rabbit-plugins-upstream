## Description:

Checks product listing images against measurable Amazon, TikTok Shop, Temu, Shopee, Shopify, and Taobao requirements, reports rejection risk, and can produce fixed images for objective geometry and color issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketplace teams, and agents use this skill to check product listing images before upload, understand objective rejection risks, and create corrected files for supported geometry and color issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled generation tooling can send prompts and images to external AI providers outside the local compliance-checking path.

Mitigation: Use scripts/check_listing.py for local checks, and invoke scripts/gen.mjs or provider CLI flows only when external processing is intended and approved for the images involved.

Risk: Pixel-level checks cannot determine whether an image contains text, watermarks, collage elements, or product defects.

Mitigation: Pair this skill with a visual review workflow or the referenced visual model check before publishing final marketplace assets.

Risk: Marketplace image requirements may change after the bundled rule table was authored.

Mitigation: Confirm current platform requirements for the target marketplace and override built-in rules with a custom rules JSON when needed.

## Reference(s):

- [Platform Image Specifications](references/platform-specs.md)
- [Provider CLI Reference](references/provider-cli.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/platform-compliance)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, code, configuration, guidance]

**Output Format:** [Human-readable Markdown or structured JSON reports, with optional generated image files when automatic fixes are requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local checker exits 0 when images pass and 1 when rejection risk remains; optional fix mode writes corrected JPEG files without overwriting source images.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
