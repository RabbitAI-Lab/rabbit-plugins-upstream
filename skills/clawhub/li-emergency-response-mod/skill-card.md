## Description: <br>
Provides structured, evidence-driven corporate emergency response with single-agent and multi-agent modes for incident management and compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[43622283](https://clawhub.ai/user/43622283) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Authorized incident responders, security teams, and developers use this skill to triage, document, contain, and report traditional IT and AI infrastructure incidents. It emphasizes evidence capture, verify-before-reporting, write-ahead logging, and human approval for high-impact response actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags bundled offensive persistence, payload, and tunnel material as requiring human review before installation. <br>
Mitigation: Install only for trained, authorized incident responders and remove or gate the offensive appendix material before broad use. <br>
Risk: Unsafe API wrapper examples and privileged response actions could cause harmful changes if treated as automated instructions. <br>
Mitigation: Use strict schemas and require human approval for deletion, process termination, DNS or hosts changes, package removal, external uploads, and privileged commands. <br>
Risk: Incident-response guidance may affect production systems if evidence capture and rollback planning are skipped. <br>
Mitigation: Configure the agent as advisory, require evidence capture and rollback planning, and approve each state-changing action through a human-in-the-loop gate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/43622283/skills/li-emergency-response-mod) <br>
- [README](artifact/README.md) <br>
- [Skill guide](artifact/SKILL.md) <br>
- [Compatibility guide](artifact/COMPATIBILITY.md) <br>
- [Multi-agent architecture](artifact/multi_agent/ARCHITECTURE.md) <br>
- [Multi-agent deployment guide](artifact/multi_agent/DEPLOYMENT_GUIDE.md) <br>
- [AI infrastructure incident response playbook](artifact/playbooks/AI基础设施应急响应手册.md) <br>
- [Linux incident response playbook](artifact/playbooks/Linux应急响应现场手册.md) <br>
- [Windows incident response playbook](artifact/playbooks/Windows应急响应现场手册.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples, JSON/YAML configuration, and generated incident reports or timelines.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory incident-response outputs; state-changing actions require human approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
