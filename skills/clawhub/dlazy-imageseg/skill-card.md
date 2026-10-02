## Description:

Separates image foregrounds from backgrounds and provides transparent-background image URLs for product photos, portraits, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to remove image backgrounds for product photos, portraits, and visual compositions through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted images may be uploaded to dLazy and result images hosted there.

Mitigation: Use only images approved for third-party cloud processing and review the service terms before upload.

Risk: Using the third-party CLI requires an API key that login may store locally.

Mitigation: Review the pinned CLI before installation and protect or revoke the API key as needed.

Risk: The documented example uses a prompt flag inconsistent with the image option shown in help.

Mitigation: Check `dlazy imageseg -h` and supply the image with `--image`.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, URLs]

**Output Format:** [Markdown with shell commands and a link to the resulting image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result images are hosted by dLazy; the CLI can also save them locally.]

## Skill Version(s):

1.3.24 (source: ClawHub release; supplied skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
