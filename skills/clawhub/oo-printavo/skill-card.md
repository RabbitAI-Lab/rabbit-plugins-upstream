## Description:

Printavo (printavo.com). Use this skill for searching and reading Printavo account data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Printavo account, token, contact, customer, order, and task data through the OOMOL Printavo connector. It supports read-focused operational lookups with filtered listing and live schema inspection before action execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Review and trust the OOMOL CLI distribution path before installation, and prefer a versioned package or verified download where available.

Risk: Connector actions or schemas may change over time, including future actions that modify Printavo data.

Mitigation: Inspect the live action schema before execution and require explicit user confirmation for any action that changes or removes data.

## Reference(s):

- [ClawHub Printavo skill page](https://clawhub.ai/oomol/skills/oo-printavo)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Printavo homepage](https://www.printavo.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and returns read action results as JSON when commands are executed.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
