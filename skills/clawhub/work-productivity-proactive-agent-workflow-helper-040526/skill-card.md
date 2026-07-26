## Description: <br>
Designs proactive agent workflows that notice recurring needs, propose timely actions, and stay bounded by permissions, evidence, and user control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent builders, operations teams, productivity system designers, and skill authors use this skill to design proactive assistant workflows with clear triggers, approval gates, cooldowns, audit records, and user-control boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat planning output as authorization to enable recurring automations, monitoring, notifications, scheduled jobs, or API integrations. <br>
Mitigation: Review proposed workflows before deployment and require explicit approval before enabling integrations, scheduled execution, notifications, or business-system actions. <br>
Risk: Broad proactive triggers can create noisy or low-value notifications. <br>
Mitigation: Define specific trigger signals, freshness checks, confidence thresholds, duplicate suppression, cooldowns, opt-out paths, and quiet periods before enabling proactive behavior. <br>
Risk: Sensitive, destructive, public, or account-changing actions could be over-automated if approval boundaries are omitted. <br>
Mitigation: Keep external sends, purchases, destructive file changes, account changes, and public publishing behind explicit user approval gates with audit records. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-proactive-agent-workflow-helper-040526) <br>
- [Proactive Agent Demand Signal](https://clawhub.ai/skills/proactive-agent) <br>
- [Self-Improving + Proactive Agent Demand Signal](https://clawhub.ai/skills/self-improving) <br>
- [Ontology Demand Signal](https://clawhub.ai/skills/ontology) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with optional code, command, configuration, checklist, and workflow sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include workflow specs, notification copy, escalation rules, cooldown state models, audit-log structures, and validation checklists.] <br>

## Skill Version(s): <br>
0.1.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
