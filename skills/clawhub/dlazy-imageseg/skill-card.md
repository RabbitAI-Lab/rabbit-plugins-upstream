## Description:

Separates image foreground from background and returns a transparent-background image URL for product imagery, character cutouts, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to remove image backgrounds for product photos, character cutouts, and visual compositions through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs are uploaded to dLazy-hosted services for processing.

Mitigation: Submit only images approved for sharing with dLazy.

Risk: Using the skill requires a dLazy API key and a third-party CLI.

Mitigation: Confirm the service and pinned @dlazy/cli@1.2.3 package are trusted before installing; keep the API key private.

Risk: The documented --prompt example conflicts with the listed --image option.

Mitigation: Check dlazy imageseg -h for the accepted options before running the command.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Image URL, Image file (optional)]

**Output Format:** [JSON response with a transparent-background image URL; optional downloaded image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before the image URL is available.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
