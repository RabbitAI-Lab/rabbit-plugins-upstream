## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route explicit task or project requests into durable loop queues, track progress, handle revisions, and verify completion evidence. It is intended for OpenClaw or Hermes workspaces where the loop CLI and integration have been deliberately installed and checked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead users to run external CLI code that installs persistent services or scheduled queue execution.

Mitigation: Pin and verify the npm package or repository commit, review generated services and schedulers before confirming installation, and run doctor and smoke checks after installation.

Risk: Dashboard exposure can broaden access if it is bound beyond localhost.

Mitigation: Keep the dashboard on localhost unless Tailnet exposure is intentionally required and governed by Tailscale ACLs or Grants.

Risk: Durable automation can continue work beyond a single chat turn if installed and scheduled.

Mitigation: Install only on hosts where durable loop automation is intended, confirm queue and worker targets before writes, and keep removal or disablement steps available.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package reference](references/npm-package.md)
- [Official distribution repository](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration paths, and operational status language]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are procedural and may include commands for installing, verifying, routing, operating, and reviewing loop queues.]

## Skill Version(s):

0.15.17 (source: server-resolved release metadata and npm package reference)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
