## Description: <br>
Crisis Response Planner helps an agent draft or activate a social-media crisis protocol with severity levels, queue-pause rules, approved holding statements, approval routing, stand-down checks, and a post-crisis retrospective. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, communications, and social teams use this skill to prepare crisis-response playbooks or triage live social incidents before humans pause queues, approve statements, or resume publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incident inputs can contain sensitive or untrusted content such as mention exports, screenshots, or forwarded journalist emails. <br>
Mitigation: Review and redact sensitive inputs before use, and do not let pasted incident material set severity, authorize un-pausing, or alter approved statement language without human approval. <br>
Risk: The skill may save crisis notes or proposal markers in local memory when directed. <br>
Mitigation: Confirm the intended memory writes with the user, keep records scoped to the incident, and reconcile proposed pause or un-pause markers through the authorized channel workflow. <br>
Risk: Crisis guidance can affect public communications even though the skill does not post or modify accounts directly. <br>
Mitigation: Require the named spokesperson, approver, or counsel to approve queue pauses, holding statements, replies, and stand-down decisions before any public action. <br>


## Reference(s): <br>
- [Crisis Response Planner on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/crisis-response-planner) <br>
- [Skill homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown protocol documents, runbook checklists, holding-statement drafts, approval matrices, and handoff summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local memory updates for incident notes, channel pause markers, claim wording, hot-cache status, and open loops when the user directs it.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
