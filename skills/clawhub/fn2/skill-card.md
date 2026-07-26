## Description: <br>
Research stocks, markets, and the economy with FN2's grounded AI, and create, schedule, and manage research agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fn2](https://clawhub.ai/user/fn2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to ask grounded market, stock, earnings, macroeconomic, and company-comparison questions through FN2. They can also create, schedule, run, pause, resume, and delete recurring FN2 research agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research prompts and agent-management requests are sent to the FN2 API. <br>
Mitigation: Install only when the user intends to use FN2, keep FN2_API_KEY private, and avoid sending sensitive prompts unless approved. <br>
Risk: FN2_API_BASE can override the default API endpoint. <br>
Mitigation: Use only a trusted FN2_API_BASE value and leave it unset for the default FN2 API. <br>
Risk: Scheduled agents can run recurring research automatically, and deleting an agent removes its history. <br>
Mitigation: Ask for explicit confirmation before creating recurring agents or deleting an agent and its history. <br>


## Reference(s): <br>
- [FN2 homepage](https://fn2.ai) <br>
- [FN2 CLI and API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/fn2/skills/fn2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown research answers, JSON API responses, and shell command invocations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FN2_API_KEY, supports optional FN2_API_BASE, and may take 30-120 seconds for research requests.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
