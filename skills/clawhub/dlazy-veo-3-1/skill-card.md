## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or extend videos through the dLazy CLI with Google Veo 3.1. It supports prompt-driven generation, frame/reference-image inputs, optional saved outputs, and asynchronous task handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and hosted dLazy service.

Mitigation: Install only if the dLazy CLI and service are trusted; use the pinned npx/on-demand path when a persistent global binary is not desired.

Risk: Prompts and selected local media files are sent to dLazy API and media storage endpoints.

Mitigation: Confirm the files and prompt content before generation, and avoid sending sensitive media or confidential prompts unless the service terms permit that use.

Risk: The dLazy API key enables billable service access.

Mitigation: Keep the key revocable, rotate it when needed, and confirm expected credit usage before running generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Invocations may return hosted media URLs or asynchronous task identifiers from the dLazy CLI.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
