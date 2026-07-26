## Description: <br>
Unified memory platform for Hermes, OpenClaw and AI agents for persistent long-term memory, cross-skill sharing, automated capture, governance rules, optimization, and pgvector search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunme1977](https://clawhub.ai/user/sunme1977) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let Hermes, OpenClaw, or similar agents capture, search, and reuse local long-term memory across sessions. It also provides guidance for optional background maintenance and governance rules around agent behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persistently stores and reuses conversation-derived personal and project context. <br>
Mitigation: Enable it only with explicit consent, keep the Sidecar local, and periodically inspect or delete stored memories that contain sensitive data. <br>
Risk: The skill can silently load and capture memory during normal agent sessions. <br>
Mitigation: Review the capture triggers before use and disable or narrow automatic capture for conversations that may contain confidential information. <br>
Risk: Optional cron jobs can run background memory capture, tagging, or reminders. <br>
Mitigation: Create background jobs only after explicit opt-in and review existing cron entries after installation or update. <br>
Risk: The skill depends on local API credentials and a memory.py CLI. <br>
Mitigation: Prefer environment-managed secrets, avoid project-local .env files in shared repositories, and run memory.py only from trusted local paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sunme1977/skills/hermesclawzero-auto-memory) <br>
- [README](README.md) <br>
- [Enforce Governance Architecture](references/enforce-architecture.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local CLI calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local Sidecar API configuration from MEM_PUBLIC_URL and API_KEY when the skill's commands are executed.] <br>

## Skill Version(s): <br>
3.0.2 (source: server release evidence; artifact frontmatter and changelog show 3.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
