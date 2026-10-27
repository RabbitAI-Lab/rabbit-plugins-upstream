## Description:

Generates audio by selecting an appropriate dLazy CLI audio or text-to-speech model from a prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate speech, dialogue, music, and sound effects from prompts or text with dLazy audio models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy and its generation providers.

Mitigation: Only submit content you are authorized to share and comfortable sending to those services.

Risk: The CLI stores an organization API key locally, and audio generation consumes service credits.

Mitigation: Keep the key private, revoke it when no longer needed, and confirm credit use before generating audio.

Risk: Installing the CLI globally adds a persistent local command-line tool.

Mitigation: Use the documented npx alternative when you want to avoid a global CLI installation.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, URLs, JSON]

**Output Format:** [Generated audio assets hosted at dLazy media URLs, with result metadata in a JSON envelope]

**Output Parameters:** [Varies by selected model; may include prompt or text, voice, language, and duration]

**Other Properties Related to Output:** [Generation uses dLazy services and consumes organization credits.]

## Skill Version(s):

1.3.34 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
