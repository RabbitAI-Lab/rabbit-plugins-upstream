## Description:

Operates 2Chat through an OOMOL-connected account using the oo CLI for reading account data, listing webhooks, checking API usage, validating API keys, and creating contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate 2Chat through an OOMOL-connected account, including contact creation, contact and webhook listing, API usage checks, and API key validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe directly into a shell.

Mitigation: Use a verified installation method for the oo CLI and review the install guide before running installer commands.

Risk: The create_contact action changes 2Chat account state.

Mitigation: Fetch the live action schema, review the exact payload and expected effect, and get user confirmation before running the command.

Risk: The skill depends on OOMOL-managed credentials and connection state.

Mitigation: Run login or connection setup only after an auth or connection error indicates it is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twochat)
- [2Chat homepage](https://2chat.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
