## Description:

Run OpenClaw-wide autonomous QA and live/stress campaigns across independent subsystem lanes, with verified fixes and a resumable evidence report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw developers and maintainers use this skill to investigate current-main bugs across subsystem lanes, verify root causes and fixes, and keep a resumable evidence ledger. It guides authorized implementation, testing, independent review, and landing of low-risk fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some local skill references were unresolved during security review, so parts of the workflow may depend on unavailable or different installed skills.

Mitigation: Review the unresolved references and confirm each referenced skill fits the workflow before relying on those steps.

Risk: The workflow can propose code changes and repository actions that affect sensitive or public-facing behavior.

Mitigation: Require explicit authorization for changes and landing, and route security, persistent-state, protocol, public-contract, and other review-sensitive changes to the appropriate maintainers.

## Reference(s):

- [Campaign evidence guidance](artifact/references/campaign-evidence.md)
- [Evidence ledger guidance](artifact/references/evidence-ledger.md)
- [Live proof routing](artifact/references/live-proof-routing.md)
- [Subsystem lanes](artifact/references/subsystem-lanes.md)
- [Auto QA on ClawHub](https://clawhub.ai/hillstreet-ph/skills/auto-qa)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown campaign reports and evidence ledgers, with code changes and verification summaries when authorized fixes are carried out]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Campaign progress and findings are recorded for resumption.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
