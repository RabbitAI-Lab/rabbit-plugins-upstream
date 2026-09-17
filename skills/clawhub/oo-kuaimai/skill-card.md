## Description:

Kuaimai ERP (kuaimai.com). Use this skill for ANY Kuaimai ERP request — searching and reading data. Whenever a task involves Kuaimai ERP, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Kuaimai ERP products, SKUs, inventory, orders, stockouts, shops, and warehouses through an OOMOL-connected account. It can also refresh the Kuaimai Open Platform session when the user explicitly requests and confirms that action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes first-time installation commands that execute remote scripts.

Mitigation: Prefer verified, pinned, or package-manager installation steps from the publisher before installing the oo CLI.

Risk: The refresh_session action changes session validity even though most listed actions are read-only.

Mitigation: Use the skill for clearly scoped Kuaimai ERP reads and run refresh_session only after explicit user request and confirmation.

## Reference(s):

- [Kuaimai ERP skill page](https://clawhub.ai/oomol/skills/oo-kuaimai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Kuaimai ERP homepage](https://www.kuaimai.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when commands are run.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
