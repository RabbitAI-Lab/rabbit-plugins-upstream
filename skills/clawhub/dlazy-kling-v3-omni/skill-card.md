## Description:

Guides agents in generating Kling V3 Omni videos from text prompts and optional media using the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through text-to-video or image-to-video generation, including authentication, CLI commands, and retrieval of generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be uploaded to the hosted dLazy service, and generated outputs are hosted remotely.

Mitigation: Only submit prompts and files you intend to share with the service; review the service terms before use.

Risk: The external npm CLI can be installed globally, and login may store an API key locally.

Mitigation: Use the on-demand npx option if a persistent install is unwanted, and protect or revoke stored credentials as needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON response guidance]

**Output Format:** [Markdown instructions with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned via hosted URLs; asynchronous requests return a task identifier.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
