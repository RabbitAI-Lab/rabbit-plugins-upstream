## Description:

GroqCloud (groq.com) skill for reading, creating, and updating GroqCloud data through OOMOL's oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect GroqCloud models, create chat completions, and run GroqCloud audio transcription or translation through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to execute remote installer scripts directly in a shell without verification.

Mitigation: Review the setup path before installing; prefer a versioned, signed, or package-manager installation source for the oo CLI.

Risk: Write actions can create chat completions, transcriptions, or translations using the connected GroqCloud account.

Mitigation: Confirm requested GroqCloud write actions and exact payloads with the user before allowing them to run.

## Reference(s):

- [ClawHub GroqCloud skill page](https://clawhub.ai/oomol/skills/oo-groqcloud)
- [GroqCloud homepage](https://groq.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing GroqCloud action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
