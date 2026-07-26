## Description: <br>
Automatically evaluates and supports human review of AI agents across memory, preference, boundary, trust, learning, expression, and CSB-AEP relationship dimensions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lilozhao](https://clawhub.ai/user/lilozhao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to run automated A2A evaluations, review raw agent responses, add human scores, and generate ranked JSON and text reports for configured agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The evaluation workflow sends personal or contextual prompts to configured local and public agents. <br>
Mitigation: Run it only against agents you are authorized to test, review config/agents.json before use, and avoid production or sensitive agents unless the operator has consented. <br>
Risk: Evaluation results may contain prompts, agent response excerpts, scores, and review comments. <br>
Mitigation: Treat eval-results/ as sensitive, restrict access to generated reports, and apply retention rules appropriate for the tested agents and users. <br>
Risk: Scheduled or external report delivery could send evaluation content outside the intended review boundary. <br>
Mitigation: Do not enable Feishu or cron delivery until the destination, payload, and recipients have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lilozhao/skills/csb-agent-eval) <br>
- [Artifact README](README.md) <br>
- [CSB-AEP v0.2 draft reference](csb-agent-evaluation-framework/CSB-AEP-v0.2-draft.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON and text evaluation reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Evaluation outputs are written under eval-results/ and may include prompts, response excerpts, scores, rankings, logs, and merge reports.] <br>

## Skill Version(s): <br>
0.2.0 (source: release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
