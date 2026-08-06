## Description: <br>
Helps agents select, adapt, and schedule recurring marketing loops with cadence, self-checks, state handling, stop conditions, and human approval guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, founders, and agents use this skill to turn recurring marketing work into scheduled loops for SEO, paid media, lifecycle, retention, revenue, referral, and operating reviews. The skill helps choose a loop, tune cadence to signal speed, define safe action thresholds, and stage outputs for review where needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A recurring marketing loop could send messages, spend money, publish publicly, change account settings, or use customer data without sufficient boundaries. <br>
Mitigation: Require human approvals for gated actions unless explicit authorization, caps, allowlists, suppression checks, and a documented kill switch are in place. <br>
Risk: A loop could act on stale, noisy, or incomplete marketing data and produce misleading recommendations or repeated actions. <br>
Mitigation: Use the skill's self-checks, durable state, idempotency rules, stop conditions, and run logs before acting on loop output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coreyhaines31/skills/marketing-loops) <br>
- [Marketing Loop Catalog](references/loop-catalog.md) <br>
- [Loop Guardrails & Compliance](references/loop-guardrails.md) <br>
- [Loop Orchestration & Rollout](references/loop-orchestration.md) <br>
- [Loop State & Run Logging](references/loop-state.md) <br>
- [Loop Template](references/loop-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with loop specifications, checklists, and scheduling recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stage drafts, reports, notifications, files, or schedule instructions depending on the selected loop.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact metadata reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
