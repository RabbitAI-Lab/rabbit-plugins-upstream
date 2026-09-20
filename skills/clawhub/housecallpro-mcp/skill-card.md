## Description:

Read a Housecall Pro estimate or invoice sent by a contractor, including line items, totals, tax, balances due, and contractor details, from a shell with curl instead of running the housecallpro-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Housecall Pro customer estimate and invoice links with shell commands, summarize payment details, and understand which actions can or cannot be scripted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro document links function as bearer credentials and may allow anyone holding the link to read an estimate or invoice and, for estimates, decline an option.

Mitigation: Keep tokens out of shared transcripts, logs, and commits; use local variables or files under user control.

Risk: The skill includes a live command that can decline a contractor estimate option.

Mitigation: Read the estimate first, manually confirm the exact option ID, name, and amount, then re-read the estimate after the request to confirm the final status.

Risk: Some endpoint notes are explicitly unverified or out of scope.

Mitigation: Prefer the verified estimate, invoice, organization lookup, and decline examples; treat unverified endpoint notes as references requiring manual review.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes guidance for handling bearer links, reading estimate and invoice JSON, declining options, and avoiding scripted approvals.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
