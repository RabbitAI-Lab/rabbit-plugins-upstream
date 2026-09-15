## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to synthesize Mandarin or English speech through the dLazy Gemini 2.5 TTS CLI and receive generated audio result links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any referenced files are processed by dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive content unless the user accepts dLazy's hosted-service handling and terms.

Risk: The skill depends on installing or invoking a third-party npm CLI.

Mitigation: Prefer the pinned npx or local install path, and review the @dlazy/cli package and source before use.

Risk: Authentication uses a dLazy API key that may be saved in local CLI configuration or supplied through an environment variable.

Mitigation: Use scoped organization keys, keep local config permissions restricted, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Security evidence notes a documentation mismatch in the output example.

Mitigation: Verify the actual returned output type, MIME type, and URL before wiring results into downstream automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return hosted generated-audio URLs, or an asynchronous task identifier when run with no-wait mode.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
