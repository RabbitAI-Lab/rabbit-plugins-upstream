## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Veo 3.1 video-generation workflow from an agent, including prompt-based generation, image-conditioned generation, and video extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media files are sent to dLazy cloud services for generation.

Mitigation: Only pass prompts and files intended for upload, and review dLazy service terms before use.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Protect the local config, rotate or revoke keys from the dLazy dashboard when needed, or provide DLAZY_API_KEY per invocation.

Risk: Global installation keeps a third-party CLI binary on the system.

Mitigation: Use the pinned npx invocation, npx @dlazy/cli@1.2.3, when avoiding a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted result URLs; asynchronous runs may return a generateId for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
