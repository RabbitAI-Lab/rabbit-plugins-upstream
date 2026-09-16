## Description:

Metronome (metronome.com). Use this skill for Metronome requests that search and read customer, invoice, billable metric, and related account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Metronome through an OOMOL-connected account, inspect live action schemas, and retrieve customer details, invoices, billable metrics, and customer lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute remote installer scripts before the oo CLI is available.

Mitigation: Review the setup path before installation, prefer an official versioned oo CLI installation method, and verify installers before running them.

Risk: Connecting Metronome through OOMOL grants the connector access to business billing and customer data within the account scope.

Mitigation: Grant only the required Metronome account scope, keep credentials server-side, and review access before connecting or reconnecting the provider.

Risk: Authentication, connection, CLI, or billing failures may require setup or recovery actions before Metronome requests can complete.

Mitigation: Run setup or recovery steps only after a matching command failure and avoid repeating sign-in or connection steps proactively.

## Reference(s):

- [Metronome homepage](https://metronome.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-metronome)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, action names, schema inspection steps, JSON payload examples, and guided recovery steps for authentication, connection, CLI, or billing errors.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
