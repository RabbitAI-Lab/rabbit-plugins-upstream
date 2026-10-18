## Description:

Generates multilingual, natural-sounding speech from text using Gemini 2.5 TTS through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can turn text prompts into spoken audio in supported languages and voices using the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the third-party dLazy CLI executes external software.

Mitigation: Review the package before use; choose the documented npx option to avoid a persistent global installation.

Risk: Prompts are sent to dLazy's cloud service, and an API key is needed for access.

Mitigation: Avoid sending sensitive prompts without approval; protect the key and rotate or revoke it from the dLazy dashboard if needed.

Risk: The documented example depicts image output for a text-to-speech skill.

Mitigation: Verify actual output type and URL before relying on or distributing generated results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI repository (CLI reference, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Audio result links]

**Output Format:** [Markdown instructions and JSON command response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous jobs may require polling. The documented image output example may be inaccurate.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; artifact frontmatter lists 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
