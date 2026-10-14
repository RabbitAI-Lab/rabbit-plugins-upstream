## Description:

Separates image foregrounds from backgrounds and returns a URL for a transparent-background image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to remove image backgrounds for product photos, portraits, and compositions through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images may be uploaded to dLazy storage, and output images are hosted by dLazy.

Mitigation: Use only images you are comfortable sending to dLazy's cloud service.

Risk: Login can save an API key locally, and a global CLI installation persists on the device.

Mitigation: Protect the local API key, review the pinned CLI package before use, and use npx @dlazy/cli@1.2.3 if a persistent installation is not desired.

## Reference(s):

- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and JSON with a transparent-image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID; generated images are hosted on dLazy, with optional local download.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; embedded frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
