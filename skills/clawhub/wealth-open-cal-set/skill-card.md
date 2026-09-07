## Description:

Turn user-supplied open windows into a four-to-eight still wealth open calendar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan and generate a consistent pack of wealth open-window calendar stills from open dates the user has already supplied and approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra device token locally and requests broad media, wallet, artifact, and task permissions.

Mitigation: Use a limited Beatra account where possible, protect the local credential files, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: Silent automatic updates can change reviewed package code before normal use.

Mitigation: Disable automatic updates with the bundled update command when reviewed code must remain fixed.

Risk: Generated wealth calendar stills may contain unreadable or incorrect small text or be mistaken for financial advice.

Mitigation: Use only user-supplied approved open-window dates, review visible text against the confirmed pack list, and avoid presenting generated stills as certified returns or buy recommendations.

Risk: Retrying billable generation work incorrectly can create duplicate tasks or charges.

Mitigation: Preserve one client request identity for each approved still and retry only unchanged requests with the same identity after transport uncertainty.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wealth-open-cal-set)
- [Beatra skill homepage](https://beatra.ai/skills/wealth-open-cal-set)
- [Wealth open calendar pack workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON payloads and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled pack plan and Beatra image-generation task requests for one still per approved open window, usually four to eight stills.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
