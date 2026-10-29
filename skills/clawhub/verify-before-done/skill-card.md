## Description:

A completion contract for agents. Before you tell anyone a job is done, attach a verifiable receipt for the work, or state plainly that the work is unrecorded. Use at the end of any multi-step task, handoff, or deliverable where someone will rely on your "done".

This skill is ready for commercial/non-commercial use.

## Publisher:

[zambodotdev](https://clawhub.ai/user/zambodotdev)

### License/Terms of Use:

MIT

## Use Case:

Agents use this completion contract at the end of multi-step tasks, handoffs, or deliverables so people relying on a completion claim can check its receipt or see that the work is unrecorded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad handover instructions can share private task details without requiring review.

Mitigation: Review and redact task details before recording or sharing them; confirm receipt visibility and retention, and use an approved private receipt service or the disclosed unrecorded fallback for confidential work.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zambodotdev/skills/verify-before-done)
- [Zambo MCP endpoint (default receipt source)](https://zambo.dev/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Text with receipt links or an explicit unrecorded notice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completion guidance may include verifiable receipt links.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
