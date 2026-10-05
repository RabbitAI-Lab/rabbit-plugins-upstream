## Description:

Helps developers deploy applications to production on their own provider accounts, with human approval for changes and checks that report what was verified.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikehasa](https://clawhub.ai/user/mikehasa)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use GoLive to plan and carry out approved production deployment and service wiring on their own accounts, then review verification results and remaining manual steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production writes or teardown can change or remove live resources.

Mitigation: Review the plan's destinations and confirmation flags, and approve each change before it runs.

Risk: Provider credentials may grant broad account access or be exposed in chat.

Mitigation: Use scoped or short-lived tokens where possible and never paste secrets into chat.

Risk: Generated .golive reports and handoffs can disclose account and resource names.

Mitigation: Treat generated reports and handoffs as sensitive and limit who can access them.

Risk: Updating the skill between planning and execution can invalidate an approval.

Mitigation: Update only between deployment runs; make a new plan and obtain fresh approval after a release change.

## Reference(s):

- [GoLive on ClawHub](https://clawhub.ai/mikehasa/skills/golive)
- [Planning and verification guide](references/plan-and-verify.md)
- [Guided provider setup](references/guided.md)
- [Update and rollback guidance](references/updates.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Verification summaries]

**Output Format:** [Text and Markdown with shell commands and structured verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment checks distinguish verified results from warnings, skipped checks, and manual handoffs.]

## Skill Version(s):

0.1.0-alpha.8 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
