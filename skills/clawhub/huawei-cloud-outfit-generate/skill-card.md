## Description:

Generates one random outfit suggestion from a bundled wardrobe, with optional style and season filters and Markdown, plain text, or JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

People looking for a daily outfit suggestion can use it to get a coordinated top, bottom, footwear, and accessory based on a chosen style and season.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A selected --output path overwrites an existing file.

Mitigation: Choose a new path or back up the existing file before using --output.

Risk: When a wardrobe lacks strict matches, style or season preferences may be relaxed; an incomplete custom wardrobe can produce missing-item placeholders.

Mitigation: Review fallback notices and ensure a custom wardrobe covers all categories and requested combinations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-outfit-generate)
- [Usage Guide](artifact/references/usage-guide.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown, plain text, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One outfit with one item per category; optional style, season, wardrobe, seed, and output-file settings.]

## Skill Version(s):

1.0.3 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
