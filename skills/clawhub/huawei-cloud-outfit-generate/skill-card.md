## Description:

Generates one outfit suggestion from a bundled wardrobe, with optional style, season, and seed controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request a complete outfit suggestion for a chosen or randomly selected style and season. Developers can also use the plain-text or JSON output in local workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writing to an existing output path overwrites that file.

Mitigation: Choose an output filename that does not contain data you need to keep.

Risk: A custom wardrobe without all four item categories may produce an incomplete outfit.

Mitigation: Provide custom wardrobe entries for tops, bottoms, footwear, and accessories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-outfit-generate)
- [Usage Guide](artifact/references/usage-guide.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)
- [Verification Method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Markdown, Plain text, JSON]

**Output Format:** [One outfit suggestion per invocation, rendered as Markdown, plain text, or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional style, season, and seed controls; a seed makes the result reproducible.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
