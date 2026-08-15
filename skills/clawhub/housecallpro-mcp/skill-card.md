## Description:

Helps agents read Housecall Pro customer estimate and invoice details from portal links using curl and jq, including totals, line items, balances, and the limits around declining or approving estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to inspect Housecall Pro customer estimate or invoice data from a shell workflow without installing an MCP server. It is suited to reading details and preparing decline requests, while approval remains a browser action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro portal links and tokens can expose private estimate or invoice data.

Mitigation: Treat every link or token as a password, keep it out of shared logs and transcripts, and do not commit it.

Risk: Declining an estimate option is a mutating action that may notify the contractor or affect the customer relationship.

Mitigation: Require explicit user confirmation before any decline request and re-read the estimate afterward to verify the result.

Risk: The artifact documents unverified endpoints outside the main estimate and invoice workflow.

Mitigation: Use only the verified estimate, invoice, organization lookup, and decline paths unless the extra endpoint has separate authorization and review.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-supplied Housecall Pro portal tokens; no MCP server is required.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
