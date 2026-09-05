## Description:

Guides agents to read Housecall Pro customer estimates and invoices with curl, summarize monetary fields correctly, look up contractor details, and decline estimate options when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to inspect Housecall Pro customer estimate or invoice links from a shell, extract totals and contractor details, and avoid unsupported scripted approval flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Housecall Pro estimate and invoice links act as bearer credentials and can expose customer document details if shared or logged.

Mitigation: Keep tokens out of commits, shared transcripts, logs, and screenshots; store them only in a controlled shell variable or local file.

Risk: The decline command performs a user-directed mutation that notifies the contractor the customer is not proceeding.

Mitigation: Read the estimate first, run the decline command only when that outcome is intended, and re-read the document afterward to confirm the status changed.

Risk: Scripted approval is unsupported and could create a binding commitment if attempted through inappropriate automation.

Mitigation: Do not script approval; open the Housecall Pro link in a browser and complete approval through the normal page flow.

## Reference(s):

- [Housecall Pro consumer API recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command-oriented guidance for handling Housecall Pro document links and JSON responses.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
