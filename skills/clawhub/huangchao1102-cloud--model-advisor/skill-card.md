## Description: <br>
Model Advisor recommends AI models for quantitative trading, coding, long-document processing, everyday chat, and privacy-sensitive tasks while balancing quality, speed, and token cost. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huangchao1102-cloud](https://clawhub.ai/user/huangchao1102-cloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI users, developers, and model-heavy workflow operators use this skill to select a suitable model for the current task and understand the tradeoff between capability, speed, privacy, and token cost. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad auto-triggering may steer model choice during normal tasks without a clear user request. <br>
Mitigation: Limit activation to explicit model-selection requests or clearly related task changes. <br>
Risk: Preference recording may store model-choice behavior or sensitive workflow context. <br>
Mitigation: Make persistence opt-in, disclose what is stored and where, and provide deletion steps. <br>
Risk: Model recommendations and token-cost estimates may become stale or inaccurate. <br>
Mitigation: Confirm current model availability, pricing, and suitability before switching models. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huangchao1102-cloud/skills/model-advisor) <br>
- [Model Selection Rules](references/model_rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown recommendation with task classification, model choice, rationale, token-cost level, and optional /model command.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommendations may include fallback model choices and cost estimates; users should confirm model availability and pricing.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
