## Description:

Mailtrap helps agents operate Mailtrap through an OOMOL-connected account, including reading, creating, updating, and deleting Mailtrap resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to have an agent inspect live action schemas and run Mailtrap connector actions for inboxes, messages, projects, contacts, templates, domains, lists, and account data through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad oo CLI authority against the user's OOMOL-connected Mailtrap account.

Mitigation: Install only if granting agent access to the connected Mailtrap account is acceptable, and review requested actions before execution.

Risk: Write and destructive Mailtrap actions can change or remove account data.

Mitigation: Require explicit confirmation of the exact payload, target, and expected effect before running write or destructive actions.

Risk: Setup guidance includes pipe-to-shell installation commands.

Mitigation: Prefer verified or manual oo CLI installation before running connector commands.

Risk: Inline JSON payload construction can be fragile for user- or message-derived content.

Mitigation: Fetch the live action schema first and use file-based JSON payloads such as --data @path/to/file.json for complex or untrusted content.

## Reference(s):

- [ClawHub Mailtrap skill page](https://clawhub.ai/oomol/skills/oo-mailtrap)
- [Mailtrap homepage](https://mailtrap.io/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands that call Mailtrap connector actions and return JSON responses.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
