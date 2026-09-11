## Description:

Converts static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and agents use this skill to call the dLazy Vidu Q2 image-to-video workflow from prompts and input images, optionally saving generated video assets or polling asynchronous jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends prompts, selected parameters, and referenced image, video, or audio files to the dLazy cloud service.

Mitigation: Use the skill only with content appropriate for dLazy processing, and review the service terms before sending sensitive media.

Risk: Authentication depends on a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Use least-privilege handling for the key, rotate or revoke it if exposure is suspected, and avoid sharing command transcripts containing credentials.

Risk: Installation uses the third-party dLazy npm CLI package.

Mitigation: Prefer npx or an isolated environment when avoiding a persistent global binary, and decide whether the dLazy CLI package and service are trusted before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing generation status and hosted output URLs; asynchronous runs can return a task identifier for polling.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
