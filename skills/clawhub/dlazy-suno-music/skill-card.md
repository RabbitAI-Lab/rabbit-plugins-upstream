## Description:

Generates Suno music from prompts in inspiration or custom mode, with vocals or as instrumental tracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate vocal or instrumental Suno music from a prompt, with optional custom lyrics, title, style, and vocal settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media are sent to dLazy services for generation.

Mitigation: Use the skill only for content you are comfortable sharing with dLazy, and avoid including sensitive prompts or media.

Risk: The dLazy organization API key is saved in local CLI configuration unless supplied through the environment variable option.

Mitigation: Protect the saved key, use DLAZY_API_KEY when appropriate, and rotate or revoke the key from the organization dashboard if exposed.

Risk: Music generation consumes service credits.

Mitigation: Use the documented --dry-run option to inspect the payload and cost estimate before submitting a generation request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)
- [dLazy credits](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated music audio with JSON result metadata and hosted asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tracks may include vocals or be instrumental; asynchronous requests can return a task identifier before the audio is ready.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
