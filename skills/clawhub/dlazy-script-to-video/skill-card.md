## Description:

Turns a script or scene breakdown into a storyboarded, shot-by-shot video workflow using the dLazy CLI and hosted storyboard agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and production teams use this skill to send script-to-video tasks to dLazy's storyboard workflow, continue project-scoped sessions, and attach reference files when generating multi-shot animated shorts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and options to api.dlazy.com and uploads attached local files to files.dlazy.com.

Mitigation: Use only when intending to use dLazy's hosted service, avoid attaching sensitive local files, and review the files selected for upload.

Risk: The dLazy CLI requires an API key stored in local configuration or supplied through the DLAZY_API_KEY environment variable.

Mitigation: Protect the API key, prefer OS-user-restricted config permissions, and rotate or revoke the key from the dLazy dashboard when it is no longer needed.

Risk: A persistent global CLI install may remain on the system after use.

Mitigation: Use the pinned npx invocation when a non-persistent CLI execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown/text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate hosted dLazy storyboard/video generation and return streamed CLI output; attached local files are uploaded to dLazy storage before use.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
