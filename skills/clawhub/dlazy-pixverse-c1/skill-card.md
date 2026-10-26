## Description:

Generates PixVerse C1 videos from text prompts, reference images, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to request short videos from PixVerse C1 with text prompts, reference images, or start and end frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are uploaded to dLazy services, and generation may consume paid credits.

Mitigation: Avoid submitting sensitive prompts or media, preview requests with --dry-run, and review expected credit use before generating.

Risk: The CLI stores an API key in the user's local configuration.

Mitigation: Prefer device-code login over sharing a key in chat, protect the saved key, and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated media asset or URL, JSON task/result response, and CLI command text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video duration 1–15 seconds, selectable resolution and aspect ratio, and optional generated audio.]

## Skill Version(s):

1.2.34 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
