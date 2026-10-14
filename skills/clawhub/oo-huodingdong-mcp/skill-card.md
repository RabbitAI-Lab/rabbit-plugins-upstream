## Description:

Helps agents work with Huodingdong ERP data through an OOMOL-connected account, including reading records and carrying out approved changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and developers can inspect Huodingdong ERP products, inventory, orders, fulfillment, and reports, and request confirmed changes to business data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ERP actions can import, update, or delete business data.

Mitigation: Confirm the exact action, targets, and payload with the user before making changes; require explicit approval for destructive operations.

Risk: The connected account may grant broader ERP access than needed.

Mitigation: Limit the OOMOL connection to the scopes required for the task.

Risk: Installing a command-line tool runs external code.

Mitigation: Review the oo CLI installer before running it; install only when the tool is needed.

## Reference(s):

- [Huodingdong ERP MCP on ClawHub](https://clawhub.ai/oomol/skills/oo-huodingdong-mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Huodingdong ERP](https://www.huodingdong.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with ERP results and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action results depend on the connected account and current tool schemas.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
