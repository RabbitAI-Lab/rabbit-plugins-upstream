## Description:

Alibaba Bailian qwen3-tts text-to-speech for generating speech from text with curated system voices, dialect options, or a custom voice described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate text-to-speech audio through the dLazy CLI, selecting a system voice or designing a voice with a natural-language description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy's hosted service and generated media URLs are hosted remotely.

Mitigation: Avoid submitting sensitive text unless the user's data handling requirements allow use of the hosted service.

Risk: API keys may be exposed if pasted into shared shells or stored with overly broad local file permissions.

Mitigation: Prefer dlazy login, rotate or revoke exposed keys, and check that ~/.dlazy/config.json is readable only by the current OS user.

Risk: The documented output example is inaccurate because qwen-tts should produce audio or media URLs, not a PNG image result.

Mitigation: Validate actual command output before wiring this skill into an automated workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated audio or media URLs, plus optional downloaded files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous waiting, asynchronous task IDs, dry runs, configurable voices, language selection, and optional local saving.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
