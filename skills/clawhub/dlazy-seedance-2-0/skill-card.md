## Description:

Guides agents to generate Seedance 2.0 videos from text prompts or image, video, and audio references using dLazy's hosted CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate videos from text or supplied media references, including first- and last-frame inputs, through dLazy's service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy-hosted endpoints.

Mitigation: Share only content approved for this third-party service; confirm that you trust the service before use.

Risk: Installing the dLazy CLI runs a third-party package.

Mitigation: Review and trust the package before installation; use the documented pinned npx invocation if a global installation is undesirable.

Risk: CLI authentication may save an API key locally.

Mitigation: Use DLAZY_API_KEY for per-invocation authentication if you prefer not to save the key in local configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI repository (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files]

**Output Format:** [CLI guidance and JSON results with generated media URLs; optionally a saved media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of a completed result.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
