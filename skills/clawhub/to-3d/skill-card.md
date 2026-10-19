## Description:

Turns flat-lay garment photos into dimensional ghost-mannequin product images while preserving garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams turn flat-lay clothing photos into dimensional product images for online listings without photographing a model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos and prompts are sent to the selected external image provider.

Mitigation: Confirm the provider and obtain permission to upload the source images before generation; use dry-run or doctor mode to inspect the request.

Risk: Generation uses provider credentials and may incur charges.

Mitigation: Keep credentials in the supported user configuration or environment and use dry-run to review the request before running it.

Risk: Generated images may alter garment details or include unwanted body or mannequin elements.

Mitigation: Review color, texture, proportions, and visible supports before using images in a product listing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider setup and outputs](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and generated product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved to a specified path; JSON output is optional.]

## Skill Version(s):

1.0.23 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
