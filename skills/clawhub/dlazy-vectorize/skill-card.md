## Description:

Converts PNG and JPG images into color vector SVGs and returns a hosted result URL for logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to turn raster logos, icons, and flat illustrations into scalable vector assets through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images passed as local paths may be uploaded to dLazy, and outputs are hosted by dLazy.

Mitigation: Confirm the images are suitable for third-party processing before submitting them.

Risk: Login can save a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: Installing the external dLazy CLI adds a third-party dependency.

Mitigation: Review the linked source and package before installation; use the documented npx option if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Image URL]

**Output Format:** [Markdown instructions and CLI JSON response containing a hosted result URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local download; asynchronous requests may initially return a task ID instead of a result URL.]

## Skill Version(s):

1.2.27 (source: ClawHub release; artifact frontmatter: 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
