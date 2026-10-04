## Description:

Creates a coordinated set of project handover sign stills from contractor-confirmed sign titles, project details, and statutory inscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Contractors and supervisors use this skill to plan and produce three matching handover sign stills from confirmed inscriptions, then extend the approved design to the remaining signs in a project set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared full-scope device token grants broad account authority.

Mitigation: Review requested access before authorizing the Beatra connection and keep the device token private.

Risk: Approved image-generation requests spend wallet credits; additional signs and edits may incur further charges.

Mitigation: Review the current price and approve each paid batch or correction before submission.

Risk: The installed package updates its own files automatically without separate confirmation.

Mitigation: Disable automatic updates if manual review of package changes is required.

Risk: The skill can register the installation and cancel tasks when requested.

Mitigation: Review account and installation access before use; confirm cancellations explicitly.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/project-handover-sign-set)
- [Beatra skill homepage](https://beatra.ai/skills/project-handover-sign-set)
- [Project handover sign workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Markdown, Images, Guidance]

**Output Format:** [Labeled sign plan and image stills with delivery details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Initial stills require approval; later signs require separate approval and may incur charges.]

## Skill Version(s):

0.1.8 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
