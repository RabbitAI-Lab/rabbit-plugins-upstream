## Description:

Generates images from text prompts with Jimeng through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text prompts and optional reference images into generated images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be uploaded to the third-party dLazy service, and generated images are hosted there.

Mitigation: Avoid submitting sensitive prompts or media; review what you send and where results are hosted.

Risk: Installing the dLazy CLI globally and signing in may leave a persistent local API key.

Mitigation: Use the on-demand npx option or a per-invocation API key where possible, and rotate or revoke saved keys when needed.

## Reference(s):

- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)

## Skill Output:

**Output Type(s):** [Image URLs, Image files, Text]

**Output Format:** [JSON with image URLs or task status; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of an immediate image.]

## Skill Version(s):

1.3.30 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
