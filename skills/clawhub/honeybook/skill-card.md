## Description:

This skill helps agents work with HoneyBook client-portal data, including vendor contracts, invoices, questionnaires, workspace files, payment methods, and deep links for signing or payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users managing HoneyBook client portals can ask an agent to review vendor workspaces, contracts, invoices, questionnaires, and payment methods. The skill can also provide confirmed deep links for signing contracts or paying invoices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HoneyBook magic links or questionnaire links can grant access to client-portal data and the resulting credentials are cached locally.

Mitigation: Use the skill only on a trusted machine, provide portal or questionnaire links only when intended, and remove the ~/.honeybook-mcp credential files when access is no longer needed.

Risk: Ambiguous signing or payment requests could target an unintended HoneyBook vendor, contract, or invoice.

Mitigation: Specify the relevant vendor or document and require explicit confirmation before returning signing or payment deep links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or text responses with HoneyBook portal data, summaries, status details, and deep links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require user-provided HoneyBook magic links or questionnaire links; signing and payment deep links require explicit confirmation.]

## Skill Version(s):

0.8.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
