## Description:

Wavespeed helps agents generate or edit AI media by selecting WaveSpeed models, confirming parameters, and running the wavespeed CLI on the user's machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsonbuilds](https://clawhub.ai/user/johnsonbuilds)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative teams, and external agent users use this skill to create, edit, animate, upscale, or transform images, video, audio, and 3D assets through WaveSpeed models while confirming parameters before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users to run an unpinned WaveSpeed CLI package.

Mitigation: Prefer a pinned, locally scoped CLI install and review the package before use.

Risk: WaveSpeed API keys may be exposed if pasted into chat or placed directly on command lines.

Mitigation: Use the browser-based wavespeed login flow, avoid sharing live keys in chat, and rotate any key that was exposed.

Risk: Media generation can incur cost, use slow models, or run with unintended parameters.

Mitigation: Confirm the selected model, prompt, key parameters, price, and expected duration with the user before execution.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/johnsonbuilds/awesome-hermes-skills/tree/main/creative/wavespeed)
- [WaveSpeed access key page](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce WaveSpeed output URLs or downloaded files after user-approved CLI runs.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
