## Description:

Rehearse an OpenClaw update with exact package evidence, installation coverage, and existing Kova reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pdurlej](https://clawhub.ai/user/pdurlej)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill before an OpenClaw upgrade to collect package, installation, Kova, and coverage evidence, identify compatibility gaps, and prepare migration, rollback, and post-start verification plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads package metadata, downloads npm package evidence, writes local evidence artifacts, and may hash explicitly declared observation paths.

Mitigation: Run it only for intended OpenClaw upgrade rehearsals and review the generated evidence before any operator action.

Risk: Advisory reviews can expose sensitive context if secrets, private conversations, live configuration values, or production logs are supplied.

Mitigation: Use only public-safe advisory inputs and exclude secrets, private conversations, live configuration values, and raw production logs.

Risk: The optional benchmark advisory adapter executes a local program selected by the user.

Mitigation: Use the benchmark advisory adapter only with a local executable that is already trusted.

Risk: A successful rehearsal is preflight evidence, not proof of live runtime behavior or approval to mutate production.

Mitigation: Require separate operator approval, verified rollback evidence, a maintenance window, and fresh post-start checks before any live update.

## Reference(s):

- [Evidence Contract](references/evidence-contract.md)
- [Stateful Upgrades with Kova and OpenClaw](references/kova-upgrade-rehearsal.md)
- [Safe-update Phase Handoffs](references/phase-handoffs.md)
- [Field Report: OpenClaw 2026.9.1-2026.9.3](references/field-report-2026-09.md)
- [v1.3 Exit Decision](references/v1.3-decision.md)
- [ClawHub Skill Page](https://clawhub.ai/pdurlej/skills/safe-upgrade-rehearsal)
- [Project Homepage](https://github.com/pdurlej/openclaw-skill-safe-update)
- [OpenClaw Skills Contract](https://docs.openclaw.ai/tools/skills)
- [OpenClaw Update Guide](https://docs.openclaw.ai/install/updating)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and generated local JSON and Markdown evidence artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are preflight evidence and plans; they do not authorize production mutation or operator approval.]

## Skill Version(s):

1.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
