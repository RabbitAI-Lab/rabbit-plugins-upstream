## Description:

Generates 1–22-second sound effects from text prompts for foley, ambience, alerts, and games through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short sound effects for video, games, interfaces, and other media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation settings are sent to the dLazy service, which hosts generated outputs.

Mitigation: Confirm the service is appropriate before submitting sensitive prompts or sharing output URLs.

Risk: The dLazy CLI is installed from npm and login may store an API key locally.

Mitigation: Review the package before installation and protect or revoke locally saved credentials when needed.

Risk: The documented output MIME type may be inaccurate.

Mitigation: Check the actual response and file format before processing generated media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include a hosted sound-effect URL, an optional downloaded file, or an asynchronous task ID.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
