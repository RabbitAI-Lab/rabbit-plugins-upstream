## Description:

Generate and edit high-quality images with Nano Banana 2.0, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through dLazy's Nano Banana 2 command-line workflow, including text-to-image and image-to-image requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party npm CLI and requires a dLazy API key.

Mitigation: Use the pinned `npx @dlazy/cli@1.2.3` invocation when possible and rotate or revoke the API key when the skill is no longer needed.

Risk: Prompts and selected media files are sent to dLazy's cloud API for generation.

Mitigation: Avoid passing sensitive prompts or files unless the user accepts dLazy's cloud processing model.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs or downloaded image files; asynchronous mode returns a task identifier.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
