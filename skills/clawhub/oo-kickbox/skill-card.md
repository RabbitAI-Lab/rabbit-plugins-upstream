## Description:

Kickbox lets an agent verify individual email addresses and check disposable email providers through an OOMOL-connected Kickbox account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route Kickbox-related tasks through an OOMOL-connected account, including email deliverability verification and disposable email checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include curl-to-bash and PowerShell iex installer commands for the oo CLI.

Mitigation: Review installation steps before use and prefer a verified, pinned, checksum- or signature-validated oo CLI installation method outside the agent workflow.

Risk: Kickbox actions depend on live connector schemas and an OOMOL-connected account.

Mitigation: Fetch the action schema before constructing payloads and only run setup or connection steps after an auth, scope, connection, or billing failure.

## Reference(s):

- [Kickbox homepage](https://kickbox.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kickbox)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live connector schema inspection before running Kickbox actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
