## Description:

Converts storyboard context into a canvas-ready video generation pipeline with shared audio and scene inputs plus per-storyboard cloned-audio and video elements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to transform storyboard details into a structured video-generation pipeline that can be added to a canvas. It supports workflows that combine dialogue text, scene imagery, cloned audio, and generated video clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent dLazy credentials may be stored in a user configuration file.

Mitigation: Prefer the npx flow or the DLAZY_API_KEY environment variable when a long-lived saved credential is not desired, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: Prompts, parameters, and local media files may be sent to dLazy-hosted API and file services.

Mitigation: Use the skill only for media you are comfortable sending to dLazy, and review input paths before running generation commands.

Risk: The skill can add generated pipeline objects to a canvas and requires terminal execution.

Mitigation: Review the generated pipeline and run one command at a time only after confirming the intended canvas and generation action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON pipeline content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces canvas pipeline instructions and may reference generated media URLs returned by the dLazy service.]

## Skill Version(s):

1.2.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
