## Description:

GroqCloud (groq.com). Use this skill for GroqCloud requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate GroqCloud through the oo CLI, including chat completions, audio transcription, audio translation, and model metadata retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Inspect installer files and verify integrity against official OOMOL documentation before execution.

Risk: The skill routes GroqCloud actions through OOMOL as an intermediary.

Mitigation: Install only when that intermediary is acceptable for the intended data and account context.

Risk: Write actions can create chat completions, audio transcriptions, or audio translations.

Mitigation: Confirm the exact payload and intended effect before running tagged write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-groqcloud)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [GroqCloud Homepage](https://groq.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can return JSON responses from oo connector actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
