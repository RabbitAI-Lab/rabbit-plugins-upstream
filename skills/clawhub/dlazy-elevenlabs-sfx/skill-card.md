## Description:

Generates short sound effects from text descriptions for foley, ambience, alerts, and games using ElevenLabs through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request 1–22-second sound effects from text prompts for media, interfaces, and games.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or explicitly supplied media files are sent to dLazy's hosted service.

Mitigation: Confirm the user is comfortable sharing these inputs before submitting them.

Risk: Installing an external CLI and using a dLazy API key expose package-trust and credential risks.

Mitigation: Review the CLI before installation, use on-demand npx if a global install is unwanted, and rotate or revoke the key when needed.

Risk: The example response shows an image rather than an audio asset.

Mitigation: Check the actual output type and file before presenting it as a sound effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and shell commands; the CLI returns JSON with generated asset URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent can provide a hosted sound-effect link or save the generated asset locally when requested.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
