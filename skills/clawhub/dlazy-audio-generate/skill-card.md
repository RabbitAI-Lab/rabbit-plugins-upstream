## Description:

Generates music, sound effects, and text-to-speech audio by selecting an appropriate dLazy CLI audio model from the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to route audio-generation requests to the right dLazy CLI model for TTS, multi-speaker dialogue, music, sound effects, and voice search workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly provided media files are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or media unless the user is comfortable with dLazy processing and hosting generated outputs.

Risk: The dLazy CLI can store an API key under the user's profile and use paid account credits.

Mitigation: Use the npx form when a persistent global install is not desired, review @dlazy/cli before use, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill selects a dLazy subcommand, checks its help output, and guides execution through the dLazy hosted API.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter reports 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
