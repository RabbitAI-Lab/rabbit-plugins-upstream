## Description:

Enables an agent to place and manage user-authorized US phone calls, configure calling preferences, and handle inbound answering through ClawCall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shreyjindal81](https://clawhub.ai/user/shreyjindal81)

### License/Terms of Use:

MIT-0

## Use Case:

External users can delegate US business calls, scheduling and order follow-ups to an agent, or configure their ClawCall calling profile and inbound answering. The agent can report call outcomes or connect the user for a live handoff.

### Deployment Geography for Use:

United States (phone calls only)

## Known Risks and Mitigations:

Risk: Real calls or account changes may incur charges or exceed the user's intended scope.

Mitigation: Review and authorize each calling task and decision limit; explain costs and recording behavior when relevant.

Risk: The skill may use or store a ClawCall API key.

Mitigation: Keep the key in a secret store or secure local file, and send it only to the ClawCall API, never to public guides or logs.

Risk: A call may require sensitive information, and a live handoff may still be recorded or transcribed.

Mitigation: Do not collect or relay restricted information; arrange live user handoff or stop that step, without claiming the handoff is private or unrecorded.

## Reference(s):

- [ClawCall skill release](https://clawhub.ai/shreyjindal81/skills/clawcall)
- [ClawCall public guides](https://api.clawcall.dev/guides/v1/index.md)
- [ClawCall website](https://clawcall.dev)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Call outcomes and account changes are reported to the user.]

## Skill Version(s):

2.0.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
