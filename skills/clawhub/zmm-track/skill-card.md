## Description:

詹明明·有什么到期了 is a cross-session tracking skill that records commitments, expiry dates, watch-items, in-flight work, and publish queues, then surfaces due items without re-litigating the original trigger condition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to persist future review points, commitments, expiry dates, monitoring items, partially completed work, and publish queues across sessions. It is intended for workflows where due items should be resurfaced later with their original condition and action preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local tracking files may retain sensitive commitment, client, amount, or contract details.

Mitigation: Avoid storing sensitive names, amounts, or client details; use aliases or redacted descriptions for long-lived records.

Risk: Broad natural-language trigger phrases may surface saved tracking items when the user did not intend to query them.

Mitigation: Prefer explicit /zmm-track invocation for private or sensitive tracking workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-track)
- [ClawHub publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown tracking files and concise text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates persistent local tracking records for due dates, conditions, actions, and status when configured.]

## Skill Version(s):

0.2.5 (source: ClawHub release evidence; artifact frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
