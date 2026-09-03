## Description:

Checks product listing images against marketplace upload requirements and can produce platform-specific rejection-risk reports plus geometry and color fixes for supported platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, listing teams, and automation agents use this skill to check whether product images are likely to pass marketplace image rules before upload. It helps identify issues such as background color, resolution, aspect ratio, file type, alpha channel, border, file size, and subject occupancy, then proposes or runs supported local fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud helper scripts can send prompts and product images to a configured external provider when the user invokes them.

Mitigation: Use the local check_listing.py workflow for local compliance checks, and only invoke cloud generation helpers with assets that are acceptable to share with the configured provider.

Risk: The checker covers objective pixel and file properties but does not determine whether an image contains text, watermarks, collage elements, damaged products, or other content-level defects.

Mitigation: Pair pixel-level checks with visual review or a suitable content inspection workflow before publishing listing images.

Risk: Marketplace image rules can change after the bundled platform thresholds are released.

Mitigation: Confirm current platform documentation for the target marketplace and override built-in thresholds with a custom rules JSON when needed.

## Reference(s):

- [Platform Image Specifications](references/platform-specs.md)
- [Provider CLI Reference](references/provider-cli.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/platform-compliance)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON results from the checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create fixed image files when the user invokes the local checker with --fix; cloud generation helpers can produce image files when separately invoked.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
