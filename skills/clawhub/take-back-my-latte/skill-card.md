## Description: <br>
Analyze OpenAI Usage and Costs JSON, show actual spend in lattes, and estimate how many lattes the user could recover next month. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to locally analyze OpenAI Costs and optional Usage JSON exports, summarize actual spend, and estimate directional cost recovery in latte terms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OpenAI Costs or Usage exports may contain project, model, request, or billing details. <br>
Mitigation: Run the analyzer locally only on files the user is comfortable processing, and do not upload, retain, or reproduce raw Usage JSON. <br>
Risk: Usage-only exports contain token counts but not actual charges, so price estimates could be misleading. <br>
Mitigation: Request an OpenAI Costs JSON export before reporting spend, and do not invent prices from usage data. <br>
Risk: Recovery amounts are directional estimates and may not translate into guaranteed savings. <br>
Mitigation: Label recoverable cost as an estimate, include the stated recovery basis, and validate any optimization with a small test. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/margaretzybgl/skills/take-back-my-latte) <br>
- [Supported input formats](references/input-formats.md) <br>
- [Take Back My Latte action site](https://take-back-my-latte.margaret-zybgl.chatgpt.site) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with inline shell commands and analyzer JSON interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are kept under 250 words by default and include warnings when input exports are incomplete or mismatched.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
