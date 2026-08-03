## Description: <br>
Reference skill for ai-assistant API and ai-provider SDK details, including model IDs, pricing, parameters, streaming, tool use, agents, caching, token counting, and model migration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill as a reference for ai-assistant API and ai-provider SDK work, including API parameters, integration patterns, streaming, tool use, caching, token counting, and migration tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution for a broad API/reference automation role. <br>
Mitigation: Allow shell commands only for explicit, reviewed actions and avoid running commands that are not directly required by the user request. <br>
Risk: The artifact discusses API keys, credentials, rate limits, and data handling. <br>
Mitigation: Do not provide secrets unless required for a trusted task, prefer environment-scoped credentials, and review outputs before using them in production workflows. <br>
Risk: The release security verdict is suspicious because the skill scope is broad and vaguely described. <br>
Mitigation: Review the skill before installation and use it only when the requested API/reference task is clear. <br>


## Reference(s): <br>
- [Skill homepage](https://skillhub.cn) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/claude-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference API credentials, rate limits, retries, file handling, and command execution depending on the requested task.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
