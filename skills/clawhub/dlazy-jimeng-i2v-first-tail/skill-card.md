## Description:

Generate coherent transition videos from provided first and last frame images using Jimeng's first-tail image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Jimeng first-tail image-to-video workflow, supplying a prompt plus first and last frame images to generate a transition video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image paths supplied to the skill are uploaded to dLazy media storage for model processing.

Mitigation: Pass only media intended for upload, avoid sensitive images, and use hosted URLs or dry-run mode when validating inputs.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local config file, avoid exposing DLAZY_API_KEY in logs or shell history, and rotate or revoke keys from the dLazy dashboard if needed.

Risk: The workflow depends on a third-party cloud service and hosted output URLs.

Mitigation: Install only for intended dLazy/Jimeng use and review dLazy account, service, and data-handling requirements before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source listed in metadata](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to run the dLazy CLI with prompt, firstFrame, lastFrame, duration, dry-run, async, and timeout options; generated result URLs are returned by dLazy.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
