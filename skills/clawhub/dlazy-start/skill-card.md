## Description: <br>
Dlazy Start helps AI orchestrators drive @dlazy/cli for installation, authentication, capability discovery, cloud and local tool invocation, async task polling, and common failure recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
AGPL-3.0-or-later <br>


## Use Case: <br>
Developers and AI orchestrator users use this skill to operate @dlazy/cli consistently, including discovering available tools, preparing JSON inputs, running cloud or local media commands, polling asynchronous jobs, and recovering from common CLI failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to use browser session cookies for downloads when handling anti-bot challenges. <br>
Mitigation: Allow cookies_from_browser only after explicit user approval for that specific download, and avoid logging or reusing cookie-derived inputs. <br>
Risk: The CLI uses an API key, cloud media services, local media tools, and optional runtime installers. <br>
Mitigation: Install and invoke it only when the user accepts those access requirements, keep credentials out of logs, and review commands before running paid or local-install operations. <br>


## Reference(s): <br>
- [Dlazy Start on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-start) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [@dlazy/cli source reference](https://github.com/dlazyai/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON input conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to discover the live CLI tool surface before invoking commands.] <br>

## Skill Version(s): <br>
2.0.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
