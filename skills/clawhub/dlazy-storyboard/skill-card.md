## Description:

This skill helps agents create multi-shot animated storyboard projects, including scripts, character and shot prompts, reference sheets, first and last frames, image-to-video shot clips, voice/TTS, music, sound effects, subtitles, and Remotion assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to direct the dLazy storyboard agent through its CLI for consistent-character, multi-shot animated short creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be uploaded to the external dLazy service.

Mitigation: Attach only files intended to be shared with dLazy and review organizational data-sharing requirements before use.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use normal local credential protections, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables for temporary use.

Risk: Using the hosted generation service may consume account credits.

Mitigation: Confirm project scope and available credits before starting large storyboard or video-generation runs.

Risk: A persistent global CLI install may be undesirable in constrained environments.

Mitigation: Use the documented npx invocation when avoiding a long-lived global installation is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated media project workflow artifacts through the dLazy hosted service.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
