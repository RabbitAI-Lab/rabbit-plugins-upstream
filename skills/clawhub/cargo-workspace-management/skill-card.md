## Description:

Helps agents administer Cargo workspace members, tokens, folders, environment variables, and files, and submit feedback reports and session summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to manage Cargo access and resources through the Cargo CLI, upload batch input files, and send reports to the Cargo team.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace administration can change or remove members, tokens, folders, and environment variables.

Mitigation: Grant admin access only when needed and confirm destructive actions before execution.

Risk: Token listings can expose usable credentials.

Mitigation: Avoid printing or sharing token output and store credentials in secret environment variables.

Risk: Session hooks and reports can send local context to Cargo.

Mitigation: Enable session hooks only with informed consent; review and redact commands, errors, identifiers, paths, customer data, and secrets before sending reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/cargo-workspace-management)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Token management examples](references/examples/tokens.md)
- [Session tracking examples](references/examples/sessions.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with Cargo CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cargo CLI commands return JSON; some operations require workspace-admin permissions.]

## Skill Version(s):

1.4.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
