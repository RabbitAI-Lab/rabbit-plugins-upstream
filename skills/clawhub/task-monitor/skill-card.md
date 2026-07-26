## Description: <br>
Real-time web dashboard for OpenClaw sessions and background tasks with mobile-responsive auto-refresh. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jorgermp](https://clawhub.ai/user/jorgermp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to monitor OpenClaw sessions, Discord sessions, sub-agents, and cron jobs through a local web dashboard, JSON status endpoint, and optional Markdown dashboard output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An unauthenticated dashboard bound to the LAN can expose OpenClaw session metadata and prompt excerpts. <br>
Mitigation: Run on a trusted machine, prefer binding to localhost, and add firewall or authentication before exposing it beyond the local host. <br>
Risk: Session transcripts and generated dashboards may include sensitive prompts, private instructions, customer data, or business context. <br>
Mitigation: Avoid using the skill for sensitive sessions and review dashboard or Markdown content before sharing logs or outputs. <br>


## Reference(s): <br>
- [Task Monitor on ClawHub](https://clawhub.ai/jorgermp/skills/task-monitor) <br>
- [OpenClaw Documentation](https://openclaw.org/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; runtime dashboard HTML and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs a local Node.js/Express dashboard on port 3030 and can generate DASHBOARD.md from OpenClaw session data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact files report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
