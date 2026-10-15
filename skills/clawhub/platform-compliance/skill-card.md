## Description:

Checks product listing images against marketplace image specifications, reports potential rejection issues, and optionally produces corrected images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Online sellers and listing teams use this skill to check product images for marketplace-specific size, background, format, and composition requirements before uploading them. They can request a local correction of measurable issues and recheck the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes optional media-generation tools that can send product images and prompts to external providers.

Mitigation: For local compliance checks, use only check_listing.py; avoid the generation and provider tools unless remote processing and credential-backed requests are intended.

Risk: Automatic corrections can change image framing and do not detect text, watermarks, or product defects.

Mitigation: Review the initial report before enabling fixes, inspect the corrected image, and manually review content-level issues.

Risk: Marketplace image requirements can change after the bundled rules are published.

Mitigation: Confirm current marketplace requirements and supply updated custom rules when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/platform-compliance)
- [Platform image specifications and custom rules](references/platform-specs.md)
- [Optional provider configuration and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Files, Guidance]

**Output Format:** [Text or JSON compliance report; optional corrected JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch checks support a nonzero exit status for detected rejection risks; corrections are saved separately.]

## Skill Version(s):

1.0.20 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
