## Description: <br>
Run a blameless postmortem for incidents caused by AI agents or LLM features, producing a structured analysis with trace reconstruction, layered root-cause findings, and corrective actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, incident responders, and AI product teams use this skill to analyze agent or LLM failures, reconstruct traces, identify the earliest preventable failure layer, and define corrective actions after incidents such as hallucinated user-facing facts, prompt injection, runaway tool use, or autonomous wrong actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incident traces can contain secrets, customer data, or confidential prompts. <br>
Mitigation: Review and redact traces before sharing them with the agent, and include only the evidence needed for the postmortem. <br>
Risk: Missing or incomplete traces can make failure frequency and root cause uncertain. <br>
Mitigation: Record the trace gap as a finding, mark frequency as unknown when it cannot be measured, and avoid treating a single replay as proof of rarity. <br>
Risk: Corrective actions may be too narrow if they only change a prompt. <br>
Mitigation: Include a permanent regression case and at least one guardrail, gate, or detection improvement tied to the failure layer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/agent-incident-postmortem) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/agent-incident-postmortem.html) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance] <br>
**Output Format:** [Markdown postmortem with timelines, tables, checklists, and corrective actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires incident details, trace evidence, blast radius, and detection context; includes a permanent regression case.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
