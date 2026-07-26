## Description: <br>
Provides guidance for using the agent-browser CLI to automate browser workflows with accessibility-tree snapshots and ref-based element selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to drive multi-step browser automation, inspect page state through JSON snapshots, interact with ref-based elements, and manage isolated browser sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved auth state, cookies, and localStorage can expose sensitive session material. <br>
Mitigation: Keep state files out of repositories and logs, use task-specific sessions, and delete saved state when it is no longer needed. <br>
Risk: Browser automation depends on an external CLI and can act on live sites. <br>
Mitigation: Install only when the agent-browser CLI is trusted and review browser actions before using authenticated or sensitive sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/agent-browser-ref) <br>
- [Agent Browser CLI](https://github.com/vercel-labs/agent-browser) <br>
- [Bundled agent-browser reference](references/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the external agent-browser CLI for command execution.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
