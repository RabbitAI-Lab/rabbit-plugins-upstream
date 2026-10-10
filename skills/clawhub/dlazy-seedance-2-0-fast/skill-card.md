## Description:

Generates videos from text prompts, multimodal references, or first and last frames using Seedance 2.0 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request cloud-generated videos from text, reference media, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference media supplied as local files is uploaded to dLazy's cloud service.

Mitigation: Only provide media you are comfortable uploading to dLazy.

Risk: CLI login saves an API key locally.

Mitigation: Use DLAZY_API_KEY per invocation if you do not want to persist the key.

Risk: Installing the pinned third-party CLI runs software from an external publisher.

Mitigation: Review the pinned npm CLI before installing if you do not already trust dLazy.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation responses may include hosted media URLs or asynchronous task IDs; the CLI can save resulting media locally.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
