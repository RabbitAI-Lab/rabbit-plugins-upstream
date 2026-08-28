## Description:

Standardizes release approvals with GitHub-aware checklists and deployment gates before production releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to evaluate production release readiness, prepare deployment PR gate snippets, summarize QA status, and record rollout scorecards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad release or GitHub-related requests and propose updates to PR comments, tracker items, or waiver approvals.

Mitigation: Keep normal review controls in place before posting comments, changing task status, or accepting waivers.

Risk: Release gate guidance may be incomplete or misleading if checks, blockers, rollback plans, or sign-offs are stale.

Mitigation: Review the generated gate output against current GitHub checks, tracker data, deployment inputs, and approval records before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-minister-release-health-gates)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/minister)
- [Deployment Readiness Gate](artifact/modules/deployment-readiness.md)
- [Quality Signals Gate](artifact/modules/quality-signals.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown snippets and checklist summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces release gate comments, QA handoff summaries, and rollout scorecards for PRs, issues, and tracker workflows.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
