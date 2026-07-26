## Description: <br>
Uses Gemini CLI (@google/gemini-cli) to perform web search and fact-finding, then return concise sourced summaries for up-to-date information requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fengjiajie](https://clawhub.ai/user/fengjiajie) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill when a task requires current web facts, market or news context, source links, or cross-checking recent claims through Gemini CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A crafted prompt passed through the shell wrapper could run local commands. <br>
Mitigation: Avoid the bundled shell wrapper or raw shell templates with untrusted prompt text until arguments are passed without a shell; review generated commands before execution. <br>
Risk: Prompts are sent to the local Gemini CLI using its configured account. <br>
Mitigation: Do not submit sensitive or confidential content unless that account and its data handling are approved for the task. <br>
Risk: Web search output can include stale, conflicting, or low-quality sources. <br>
Mitigation: Require links, prefer company IR or SEC filings and reputable outlets, and re-run with stricter source prompts when claims look suspicious. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fengjiajie/skills/gemini-web-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with sourced summaries and inline shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Gemini CLI; web results should be checked against reputable sources.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
