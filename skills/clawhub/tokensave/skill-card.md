## Description: <br>
Use when the user explicitly asks to analyze token waste, costs, or API bills. Finds duplicate tool calls, context bloat, model mismatch, and heartbeat waste. Analyze mode is 100% local, zero config. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[raydatalab](https://clawhub.ai/user/raydatalab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use TokenSave to analyze a specific Hermes session or request dump for avoidable token spend, duplicate tool calls, context bloat, model mismatch, and heartbeat waste. The skill should be run only after an explicit request or against a user-provided session target. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Analyze mode reads local Hermes session transcripts and cost metadata. <br>
Mitigation: Run analysis only after an explicit user request, and prefer a specific session ID or file path when possible. <br>
Risk: Pipeline mode can route API calls through TokenSave and requires an API key and network access. <br>
Mitigation: Use pipeline mode only when the user intentionally wants API calls routed through TokenSave; otherwise use local analyze mode. <br>
Risk: Waste findings, especially near-duplicate detection, can flag legitimate repeated work. <br>
Mitigation: Treat findings as diagnostics to review before applying any suggested process changes. <br>


## Reference(s): <br>
- [TokenSave ClawHub Skill Page](https://clawhub.ai/raydatalab/skills/tokensave) <br>
- [TokenSave Homepage](https://github.com/raydatalab/tokensave) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown response with copied CLI analysis output and recommended follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analyze mode is local and no-config; the separate pipeline mode requires OPENAI_API_KEY and network access.] <br>

## Skill Version(s): <br>
0.4.5 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
