## Description:

Generates 10–300 seconds of original music from a natural-language prompt for background music, ads, and short videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to generate music for background audio, advertisements, and short videos from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external CLI executes code outside the skill files.

Mitigation: Review @dlazy/cli before installation; use the documented pinned npx command if a global installation is unwanted.

Risk: Prompts and provided media files are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or files without appropriate authorization.

Risk: Logging in stores a dLazy API key locally.

Mitigation: Protect the local CLI configuration and rotate or revoke the key in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides retrieval of a hosted music result URL or saving the generated asset locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
