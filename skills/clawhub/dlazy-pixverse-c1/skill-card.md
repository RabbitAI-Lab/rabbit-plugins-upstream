## Description:

PixVerse C1 helps agents generate videos from text prompts, images, first and last frames, or visual references through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's PixVerse C1 video generation workflow from an agent, including text-to-video, image-to-video, first/last-frame-to-video, and reference-based video creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media provided to the skill may be sent to dLazy cloud services and generated output URLs may be hosted by dLazy.

Mitigation: Use the skill only for content appropriate for dLazy processing, avoid sensitive local media unless approved, and review the configured API endpoints before execution.

Risk: Video generation requires a dLazy API key and may consume account credits.

Mitigation: Authenticate with the intended dLazy organization, keep credentials protected, rotate or revoke keys when needed, and use dry-run or cost-estimate behavior before expensive requests when available.

Risk: A global CLI install persists a local binary and user configuration.

Mitigation: Prefer the pinned npx invocation when a non-persistent execution path is desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result envelopes containing generated media URLs or task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated video assets locally when the agent passes a save path.]

## Skill Version(s):

1.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
