## Description:

This skill helps agents use dLazy's storyboard CLI workflow to turn scripts or scene breakdowns into storyboarded, shot-by-shot video projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creative teams, and developers use this skill to start or continue dLazy storyboard projects that convert scripts, scenes, references, voice, audio, and subtitles into multi-shot animated video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party SaaS CLI and may send prompts or attached files to dLazy services.

Mitigation: Review prompts and files for sensitive data before use, and attach only files intended for upload.

Risk: The dLazy API key may be stored locally for CLI authentication.

Mitigation: Use the documented local config or per-invocation environment variable intentionally, and rotate or revoke the key if exposure is suspected.

Risk: A global npm install persists a third-party CLI binary on the system.

Mitigation: Use the pinned npx invocation for one-off runs if a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy CLI commands and may stream responses from the dLazy service.]

## Skill Version(s):

1.0.4 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
