## Description:

Adapts web novel material into Chinese webtoon plot breakdowns, episode tags, and per-episode scripts, with optional dLazy CLI image-generation workflow guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and adaptation teams use this skill to turn supplied web novel chapters or revision notes into structured Chinese webtoon planning and script content. It also guides agents through a dLazy CLI-backed image generation flow when visual outputs are requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to install and run an external npm CLI that sends prompts to dLazy services.

Mitigation: Review the exact CLI version and source before installation, use the pinned install command or npx alternative intentionally, and run it only in environments where network calls to dLazy are expected.

Risk: The dLazy workflow stores or uses an API key and may upload local media paths supplied by the user.

Mitigation: Use a revocable API key, prefer environment-scoped credentials where practical, avoid sensitive local files, and rotate or revoke the key after use if exposure is suspected.

Risk: The bundled behavior includes strong workflow-steering instructions that can keep redirecting the conversation back to its scripted process.

Mitigation: Keep the agent under the host application's instruction hierarchy and stop or override the workflow if it conflicts with the user's current task.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown conversation output with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language adaptation workflow; generated media URLs may be returned when the dLazy CLI workflow is used.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
