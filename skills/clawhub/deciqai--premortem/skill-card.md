## Description: <br>
Premortem helps an agent facilitate a structured pre-commitment exercise where a team imagines a plan has already failed, works backward to identify failure modes, and turns the highest-priority risks into mitigations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external teams, and decision facilitators use this skill before high-stakes or hard-to-reverse decisions to surface hidden failure modes, reduce group convergence, assign mitigations, and schedule a follow-up premortem. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may share confidential business plans or internal risk details during the premortem conversation. <br>
Mitigation: Avoid sharing confidential information unless the user intends the agent to use it in the premortem exercise. <br>
Risk: External links and market examples may be mistaken for live data or operational instructions. <br>
Mitigation: Treat external links and examples as reference material, and verify current facts before making time-sensitive business decisions. <br>


## Reference(s): <br>
- [Premortem ClawHub release page](https://clawhub.ai/deciqai/skills/premortem) <br>
- [Premortem agent metadata](https://www.deciqai.com/s/premortem.json) <br>
- [Premortem method page](https://www.deciqai.com/c/premortem) <br>
- [Sources - premortem](references/sources.md) <br>
- [Method in Action: Klein 2007 and the Mitchell-Russo-Pennington 1989 Foundation](examples/klein-2007-mitchell-russo-pennington-1989-foundation.md) <br>
- [Method in Action: Back-Casting a Failed AI Agent Startup 12 Months Out (2024-2026)](examples/backcasting-ai-agent-startup-failure-2024-2026.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown conversation and structured premortem tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill asks the agent to pause at explicit wait points in coach mode and produce a modified-plan template with failure modes, mitigations, owners, triggers, monitoring signals, escalation thresholds, and a re-premortem date.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
