## Description:

Suno music generation model that supports inspiration mode, custom lyrics, instrumental generation, and vocal tracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate music through the dLazy Suno Music CLI, including prompt-based songs, custom lyrics, instrumental output, and asynchronous generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key for CLI use.

Mitigation: Use the documented dLazy login or API key setup flow, protect local credentials, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and explicitly supplied media files are sent to dLazy hosted API and storage endpoints.

Mitigation: Install and use the skill only when third-party hosted processing is acceptable for the data being submitted.

Risk: The skill depends on the third-party dLazy CLI and hosted service availability.

Mitigation: Review the disclosed CLI package and service links before deployment, and use dry-run or no-wait modes where appropriate for operational control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated music asset URLs or asynchronous task identifiers from dLazy hosted services.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
