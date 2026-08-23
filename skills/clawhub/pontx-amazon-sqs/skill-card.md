## Description:

Integrate Amazon SQS safely through Pontx. Use for queue discovery, direct SDK or CLI setup, consumer reliability, FIFO or standard queue decisions, visibility timeouts, DLQs, polling, and explicitly approved queue mutations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to integrate Amazon SQS through Pontx, inspect queue topology, configure reliable producers and consumers, and prepare direct queue actions that require explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Direct Amazon SQS calls can change queue state or affect production message processing.

Mitigation: Verify the queue, region, action, redacted preview, and unchanged input before approving send, delete, redrive, purge-like, or other state-changing workflows.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and code guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Direct queue mutations are gated by redacted previews and explicit approval.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
