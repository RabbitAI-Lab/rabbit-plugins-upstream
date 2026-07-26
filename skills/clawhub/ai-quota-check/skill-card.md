## Description: <br>
ai-quota-check provides a unified quota dashboard and model recommendations for Antigravity, GitHub Copilot, and OpenAI Codex. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kr1json](https://clawhub.ai/user/kr1json) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI tool users use this skill to inspect provider login and quota status, then choose fallback models before coding or reasoning work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local AI provider auth and session files, which may expose account details if run on an unintended machine. <br>
Mitigation: Run it only on machines where those provider accounts are intended to be checked, and review the dashboard before sharing it. <br>
Risk: The skill can make a live Codex request to refresh rate-limit data without clear user confirmation. <br>
Mitigation: Confirm the live refresh behavior before use, and prefer an option or update that asks for confirmation before refreshing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kr1json/skills/ai-quota-check) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Guidance] <br>
**Output Format:** [Markdown dashboard with tables and model recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and codex binaries; may inspect local provider auth/session files and refresh Codex rate-limit data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
