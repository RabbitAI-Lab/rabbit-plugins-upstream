## Description:

Generates multilingual, natural-sounding speech from text with Gemini 2.5 TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill through the dLazy CLI to turn text prompts into multilingual speech using a hosted Gemini 2.5 TTS service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation parameters are sent to dLazy's hosted API.

Mitigation: Use inputs approved for the user's dLazy organization and avoid submitting sensitive content unless covered by applicable service terms.

Risk: Logging in may store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx for less persistent local state, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The artifact's output example shows an image result for a text-to-speech skill.

Mitigation: Verify the actual returned audio MIME type and URL before relying on downstream automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI metadata link](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result envelopes containing hosted generated-output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documentation describes audio generation, but the artifact includes an incorrect image-output example; verify the returned audio format before downstream use.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
