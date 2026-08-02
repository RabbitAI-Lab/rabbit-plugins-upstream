## Description: <br>
Analyze OpenAI Usage and Costs JSON, show actual spend in lattes, and estimate how many lattes the user could recover next month. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze local OpenAI Costs and Usage JSON exports, understand current spend, and receive a short directional report about potential cost recovery. It supports OpenAI exports only and does not request API keys or call the OpenAI API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OpenAI Costs and Usage exports can contain sensitive spend, project, model, or API-key identifier details. <br>
Mitigation: Use only exports the user intends to analyze, keep analysis local, and avoid reproducing raw JSON in the report. <br>
Risk: Recoverable cost is a directional estimate and may not become actual savings. <br>
Mitigation: Describe recovery as an estimate, ground suggestions in the analyzer output, and validate changes with a small production test before relying on them. <br>
Risk: Usage-only exports contain token counts but not charged amounts. <br>
Mitigation: Request an OpenAI Costs JSON export before reporting actual spend, and do not invent prices. <br>


## Reference(s): <br>
- [Supported input formats](references/input-formats.md) <br>
- [Take Back My Latte ClawHub page](https://clawhub.ai/margaretzybgl/skills/take-back-my-latte) <br>
- [Take Back My Latte website](https://take-back-my-latte.margaret-zybgl.chatgpt.site) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with local analyzer JSON as intermediate evidence] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report is kept under 250 words by default and includes a local-analysis privacy notice.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
