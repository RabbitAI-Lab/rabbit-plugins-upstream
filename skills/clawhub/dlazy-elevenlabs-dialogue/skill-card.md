## Description:

Generates multi-voice ElevenLabs eleven_v3 dialogue audio by assigning voices to dialogue lines and rendering the conversation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate character dialogue, podcasts, and short skits with multiple voices from structured dialogue lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text and any file inputs are sent to dLazy's hosted service.

Mitigation: Avoid submitting private files or sensitive dialogue text unless third-party hosted processing is acceptable.

Risk: The skill relies on a pinned third-party npm CLI.

Mitigation: Review the pinned dLazy CLI source before installation, or use npx @dlazy/cli@1.2.3 to avoid a persistent global install.

Risk: A saved dLazy API key can be reused until rotated or revoked.

Mitigation: Store the key only in the documented user config or environment variable and rotate or revoke it from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell command examples and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted generated-audio URLs or an async generation identifier; --save can download the generated asset.]

## Skill Version(s):

1.3.9 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
