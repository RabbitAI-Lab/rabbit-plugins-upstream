## Description:

Helps agents generate multilingual speech from text using Gemini 2.5 TTS through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other ClawHub users can direct an agent to turn text prompts into Chinese or English speech with a chosen voice using the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy's hosted API, and generated files are hosted by dLazy.

Mitigation: Avoid submitting sensitive content without confirming the service's data-handling terms.

Risk: Login saves an API key locally, and installing the CLI globally persists the package on the system.

Mitigation: Protect the local key and review the CLI package before installing; use the documented npx option if a global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text with CLI commands and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is hosted by dLazy; asynchronous requests can return a task ID before audio is ready.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
