## Description: <br>
Track LLM API spending per agent/session with budget alerts and CSV export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent operators, and finance teams use this local CLI to estimate LLM token costs and tally token counts from agent run logs for API spend review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence says the skill has overstated feature claims around budget alerts, CSV export, and per-agent/session tracking. <br>
Mitigation: Treat the artifact as a basic local token-cost estimator unless those advertised features are verified or added before deployment. <br>
Risk: The release evidence advises avoiding the included CI verifier against untrusted folders. <br>
Mitigation: Run the verifier only on trusted code or inside an isolated sandbox. <br>


## Reference(s): <br>
- [Agent Cost Tracker ClawHub page](https://clawhub.ai/itspremkumar/skills/agent-cost-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Terminal text or JSON, with Markdown usage guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local estimation only; no network calls are described by the evidence.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata; artifact frontmatter reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
