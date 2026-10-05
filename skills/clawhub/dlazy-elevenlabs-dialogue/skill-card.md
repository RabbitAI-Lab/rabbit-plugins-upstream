## Description:

Helps agents generate multi-voice ElevenLabs dialogue for character scenes, podcasts, and short skits through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare voice-assigned dialogue and generate audio for character scenes, podcasts, and short skits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill delegates execution to a third-party CLI that must be installed or invoked.

Mitigation: Review the CLI source and npm package before installation; use the documented pinned package version.

Risk: Dialogue text, selected parameters, and any supplied media files are sent to dLazy, which also hosts generated assets.

Mitigation: Avoid submitting confidential material without approval and review the service's data-handling terms.

Risk: Authentication can store an API key in local CLI configuration.

Mitigation: Protect the local key, limit access to its configuration, and rotate or revoke it if exposed.

Risk: Documentation examples show an image result and an unsupported prompt flag for this audio dialogue command.

Mitigation: Consult the command's current help and verify its inputs and output before relying on the examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Generated-asset links]

**Output Format:** [Markdown with CLI commands and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can relay asynchronous task status and optionally save the generated asset locally.]

## Skill Version(s):

1.3.24 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
