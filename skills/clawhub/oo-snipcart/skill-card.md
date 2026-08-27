## Description:

Snipcart helps agents operate Snipcart through an OOMOL-connected account using the oo CLI for customer and order tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Snipcart connector schemas and run OOMOL CLI actions for retrieving customers and orders, with setup guidance for authentication and Snipcart connection issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Snipcart customer and order data through an OOMOL-connected account.

Mitigation: Install and use it only when commerce-data access is intended, and scope requests to the user-approved Snipcart task.

Risk: Write-tagged or destructive connector actions can change or remove Snipcart data.

Mitigation: Inspect the live connector schema and confirm the exact payload and effect with the user before running sensitive actions.

Risk: Authentication, connection, or billing setup commands could be run unnecessarily.

Mitigation: Use first-time setup steps only after a matching command failure, such as an auth error, missing scope, expired credential, or insufficient credit response.

## Reference(s):

- [Snipcart homepage](https://snipcart.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL app connections](https://console.oomol.com/app-connections?provider=snipcart)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector schema inspection steps, action payload guidance, and user confirmation prompts for sensitive actions.]

## Skill Version(s):

1.0.1 (source: release evidence and metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
