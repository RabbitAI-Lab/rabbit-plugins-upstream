## Description:

Audio generation skill that selects an appropriate dLazy CLI audio, music, sound-effect, or text-to-speech model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate speech, dialogue, music, and sound effects through the dLazy CLI. It helps an agent choose the relevant audio model, inspect the command parameters, and run the matching generation command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on executing the third-party dLazy npm CLI.

Mitigation: Prefer npx or another isolated install over a global install, and review the CLI package before use.

Risk: Prompts, parameters, and explicitly provided media files are sent to dLazy services for generation.

Mitigation: Avoid submitting sensitive content unless that SaaS processing is acceptable for the user and organization.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the key, rotate or revoke it if compromise is suspected, and avoid exposing it in command output or logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the dLazy CLI, which returns JSON envelopes containing generated media URLs.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
