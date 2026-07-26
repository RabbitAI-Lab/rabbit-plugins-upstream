## Description: <br>
Mission control dashboard for OpenClaw - real-time session monitoring, LLM usage tracking, cost intelligence, and system vitals. View all your AI agents in one place. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use Command Center to monitor OpenClaw agent sessions, LLM usage, costs, scheduled jobs, and host vitals from a local dashboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dashboard can expose sensitive OpenClaw session, workspace, operator, and transcript-derived data. <br>
Mitigation: Bind the service to localhost or a protected interface, treat dashboard data as private, and avoid public tunnels unless separately protected. <br>
Risk: Security evidence reports write/control APIs and defaults that are less constrained than the documentation implies. <br>
Mitigation: Use a real auth mode such as token, Tailscale, or Cloudflare with a narrow allowlist before remote or shared access. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/seanford/skills/command-center) <br>
- [OpenClaw Command Center README](https://github.com/jontsai/openclaw-command-center#readme) <br>
- [OpenClaw Command Center Repository](https://github.com/jontsai/openclaw-command-center) <br>
- [Architecture Overview](docs/architecture/OVERVIEW.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces instructions for starting and configuring a local OpenClaw dashboard service.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence; artifact frontmatter, package.json, and _meta.json report 1.4.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
