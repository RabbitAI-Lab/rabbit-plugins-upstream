## Description:

Guides agents in reading Housecall Pro customer estimates and invoices with shell commands and explains how to decline an estimate option or approve it in a browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and their agents use a contractor-provided link to review estimate options, prices, contractor details, and invoice balances without running an MCP server. They may also review how to decline a selected estimate option.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document links act as bearer credentials and may expose estimates or allow a decline if shared.

Mitigation: Keep links and tokens out of shared transcripts, logs, and repositories; handle them only in controlled files or variables.

Risk: Declining the wrong estimate option can notify the contractor and cannot be reversed through this workflow.

Mitigation: List open options, confirm the exact option ID and details before declining, then reread the estimate to verify its status.

Risk: Unverified account, OTP, profile, service agreement, jobs, media, and communications endpoints extend beyond the core document-reading task.

Mitigation: Avoid those endpoints unless separately reviewed and explicitly needed; complete approvals in the browser rather than attempting to script them.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/housecallpro-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains estimate and invoice fields, amount scaling, and limits on scripted approval.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
