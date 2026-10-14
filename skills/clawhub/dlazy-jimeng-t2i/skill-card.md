## Description:

Helps an agent generate images from text prompts using Jimeng through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request Jimeng text-to-image generations, optionally supplying reference images and choosing a size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party CLI and sends prompts to a hosted service.

Mitigation: Review the pinned CLI before installing and send only prompts suitable for the dLazy service.

Risk: Local media paths supplied to the CLI may upload those files to dLazy.

Mitigation: Avoid supplying sensitive local files unless you intend to upload them.

Risk: Signing in can save an API key in local CLI configuration.

Mitigation: Use a per-invocation API key if you do not want a saved key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs]

**Output Format:** [JSON response containing generated image links and metadata; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task identifier before images are ready.]

## Skill Version(s):

1.3.29 (source: ClawHub release; supplied skill frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
