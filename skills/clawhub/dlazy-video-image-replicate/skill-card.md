## Description:

Replicates a user-provided reference image or video by studying its look and structure, then recreating that style with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to ask a dLazy hosted agent to remake reference images or videos with their own media, products, or characters while preserving the source composition and look.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached reference or product media are sent to dLazy services.

Mitigation: Send only content the user is authorized and comfortable sharing with dLazy, and review dLazy service terms before use.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Protect the local config file, use the DLAZY_API_KEY environment variable for per-run credentials when preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Project-scoped sessions can reuse prior conversation context.

Mitigation: Use a fresh project or run the documented clear command when prior context should not influence a new task.

Risk: A global CLI install leaves a persistent executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred, and review the package/source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI may upload attached local files to dLazy media storage and maintains project-scoped chat context.]

## Skill Version(s):

1.3.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
