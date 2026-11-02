## Description:

Read a Housecall Pro estimate or invoice your contractor sent you — line items, totals, tax, what is still owed, the company behind it — from a shell with plain curl, instead of running the housecallpro-mcp server. Use when you want the data without the MCP, in a script, or on a machine where the MCP isn't installed. Covers declining an option, and why approving cannot be scripted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External customers who received a Housecall Pro estimate or invoice use the skill to read line items, totals, tax, outstanding balances, and contractor details from a shell. They can also decline an estimate option after reviewing it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The document link is a bearer credential that can expose the estimate or invoice and allow an estimate option to be declined.

Mitigation: Keep document links and saved JSON private; do not paste links into shared transcripts or commit them.

Risk: Declining an estimate tells the contractor you will not proceed and cannot be reversed through this workflow; the wrong option could be selected.

Mitigation: Review the estimate and explicitly select the intended option before authorizing a decline, then re-read it to confirm the result.

Risk: Approving an estimate is a binding commitment to the quoted price.

Mitigation: Review the estimate and approve it in the Housecall Pro browser flow.

## Reference(s):

- [Housecall Pro consumer API recipes](artifact/references/recipes.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples can save estimate or invoice responses as JSON files.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
