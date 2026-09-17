## Description:

OrcaRouter helps agents read, create, and update OrcaRouter data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate OrcaRouter through an OOMOL-connected account, including listing models and creating chat completions, embeddings, or Anthropic-format messages through the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer one-liners that execute scripts directly in a shell.

Mitigation: Prefer a verified package, pinned release, checksum or signature validation, and explicit user approval before installing or signing in with the oo CLI.

Risk: Write actions can create OrcaRouter completions, embeddings, or messages using the connected account.

Mitigation: Inspect the live action schema first and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [OrcaRouter homepage](https://www.orcarouter.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub OrcaRouter skill page](https://clawhub.ai/oomol/skills/oo-orcarouter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect live connector schemas and run OrcaRouter actions; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
