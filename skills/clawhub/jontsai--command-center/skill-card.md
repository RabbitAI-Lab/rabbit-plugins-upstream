## Description: <br>
Mission control dashboard for OpenClaw - real-time session monitoring, LLM usage tracking, cost intelligence, and system vitals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jontsai](https://clawhub.ai/user/jontsai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to run a local dashboard for monitoring AI agent sessions, LLM usage, costs, scheduled jobs, and system vitals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes administrative OpenClaw dashboard capabilities that go beyond passive monitoring. <br>
Mitigation: Install it only for intended administrative use, keep the server bound to localhost or a private network, and enable a real authentication mode before remote access. <br>
Risk: Examples or local defaults may use no authentication in development contexts. <br>
Mitigation: Do not copy auth 'none' settings into shared, team, VPN, Cloudflare, or public deployments. <br>
Risk: Transcript-derived identity tracking and local persistence may surface sensitive operational data. <br>
Mitigation: Review privacy controls and disable or restrict identity/topic tracking where the workspace contains sensitive conversations. <br>
Risk: Optional Linear sync, job-control actions, and system dependency installation can change local or external state. <br>
Mitigation: Inspect and disable those behaviors unless they are required for the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jontsai/skills/command-center) <br>
- [README](artifact/README.md) <br>
- [Architecture overview](artifact/docs/architecture/OVERVIEW.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Node.js application files with Markdown setup guidance, shell commands, HTML dashboard views, and JSON/SSE API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs a local OpenClaw dashboard server; requires Node.js >=18.] <br>

## Skill Version(s): <br>
1.4.1 (source: SKILL.md frontmatter and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
