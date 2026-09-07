## Description:

Generates short text-to-video or image-to-video clips through dLazy's hosted Google Veo 3.1 Fast workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short videos from prompts, image frames, or video-extension inputs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files may be sent to dLazy's hosted service for generation.

Mitigation: Use the skill only for content that can be shared with dLazy, and avoid submitting sensitive media or confidential prompts unless approved.

Risk: The workflow depends on dLazy account credentials and may consume paid credits.

Mitigation: Use revocable API keys, prefer per-run DLAZY_API_KEY for temporary access, and monitor organization credits before running generation jobs.

Risk: Global installation of the third-party CLI persists a binary on the user's machine.

Mitigation: Prefer npx @dlazy/cli@1.2.3 for on-demand use, or verify the package and source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown instructions with bash commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or async task identifiers; --save can download generated assets locally.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
