## Description:

Scouts, qualifies, proposes, delivers fixed-scope freelance jobs, and monitors payments using a coordinated five-role agent team.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to coordinate a supervised freelance delivery workflow from opportunity scouting through proposal drafting, execution, delivery, and payment tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to run a broad freelance workflow with shell, file, inbox, marketplace, and payment-status access without enough scoping or user-control detail.

Mitigation: Review before installing, restrict connected accounts and workspaces, and require explicit user approval before applications, external messages, command execution, deliverables, or payment-related actions.

Risk: The workflow can create business commitments or send proposals on the user's behalf.

Mitigation: Keep proposal submission and client communication approval-gated, and verify pricing, scope, and truthfulness before sending.

Risk: The work-runner role may execute commands and modify deliverable files in local workspaces.

Mitigation: Use a dedicated workspace, run the included evaluation set before use, and inspect generated deliverables before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/freelance-delivery-team)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Agent responses, proposals, deliverable files, command suggestions, and workflow status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires supervised approval for applications, external messages, command execution, deliverables, and payment-related actions.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
