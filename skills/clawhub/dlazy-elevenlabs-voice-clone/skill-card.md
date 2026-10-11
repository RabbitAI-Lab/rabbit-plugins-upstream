## Description:

Helps an agent use dLazy's ElevenLabs voice-cloning command to create a custom voice from an audio sample for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to clone an authorized voice sample for ElevenLabs text-to-speech projects through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning a person's voice without consent or rights can cause harm.

Mitigation: Only use voice recordings when you have explicit permission and legal rights to process them.

Risk: Local audio supplied to the command can be uploaded to dLazy-hosted services.

Mitigation: Review the recording for sensitive content and confirm that cloud processing is acceptable before submitting it.

Risk: The included examples do not consistently match the voice-cloning command.

Mitigation: Check the installed CLI's actual help and output before invoking the command or relying on its result.

Risk: An API key saved in local CLI configuration persists beyond a single invocation.

Mitigation: Prefer a per-invocation API key when possible and review key handling before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May relay a hosted result link or an asynchronous task ID; verify actual CLI output because the supplied examples conflict with voice cloning.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
