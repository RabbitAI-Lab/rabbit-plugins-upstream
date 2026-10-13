## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run explicitly requested task or project loops with queue state, verification, revisions, progress reporting, and human approval before sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unverified package or confirming the wrong integration plan could add local services, persistent queues, or schedulers.

Mitigation: Pin and verify the npm package version, review the read-only installation plan, and confirm the platform and destination before enabling writes.

Risk: Exposing the dashboard beyond localhost could make its controls accessible to unintended users.

Mitigation: Keep the dashboard local unless Tailnet access is intended; when using Tailnet, enforce appropriate Tailscale ACLs or Grants.

Risk: Loop execution may apply patches, clean up worktrees, send external messages, or change credentials or deployments.

Mitigation: Require explicit approval for patch application, cleanup, external messages, credential changes, and deployment changes; review verification and acceptance evidence before claiming completion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package command reference](artifact/references/npm-package.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown with shell commands and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite queue, task, project, and verification artifacts.]

## Skill Version(s):

0.16.0 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
