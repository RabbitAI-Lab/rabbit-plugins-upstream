## Description:

Separates an image's foreground from its background and returns a transparent-background image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and product teams use this skill to remove image backgrounds for product photos, character cutouts, and compositions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media may be uploaded to dLazy cloud storage for processing.

Mitigation: Review which files you submit and the dLazy service terms before processing sensitive media.

Risk: Signing in or saving an API key persists credentials in local CLI configuration.

Mitigation: Decide whether to store the key locally or pass it per command using DLAZY_API_KEY; rotate or revoke keys if needed.

Risk: Installing the third-party CLI runs external package code.

Mitigation: Review the linked CLI source and package before installing the pinned version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns a transparent-background image URL; an optional command saves the image locally.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release metadata; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
