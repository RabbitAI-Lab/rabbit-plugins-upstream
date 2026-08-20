## Description:

Read a Housecall Pro estimate or invoice your contractor sent you, including line items, totals, tax, amount owed, and contractor details, from a shell with plain curl instead of running the housecallpro-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect their own Housecall Pro customer estimate or invoice from a shell, summarize money fields correctly, identify the contractor behind the document, and understand why approval must happen in the browser. It also explains the one supported mutation, declining an estimate option, and how to verify that action afterward.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro document links act as bearer credentials and can expose estimate or invoice details to anyone who holds the link.

Mitigation: Use the skill only with documents you are authorized to view, keep tokens out of shared transcripts, logs, and commits, and store them only in variables or files you control.

Risk: Declining an estimate option is a real action visible to the contractor and may not be reversible from the shell workflow.

Mitigation: Read the estimate first, decline only when intentional, and re-read the estimate afterward because a 2xx response alone is not proof of the final state.

Risk: Unverified endpoints listed from the application bundle may have different scope or behavior than the verified customer-document recipes.

Mitigation: Prefer the verified estimate, invoice, organization lookup, and decline recipes; avoid experimenting with unverified endpoints unless you understand the account-scope implications.

## Reference(s):

- [Housecall Pro consumer API recipes](artifact/references/recipes.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recipes and explanatory guidance; it does not produce or store Housecall Pro document data.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
