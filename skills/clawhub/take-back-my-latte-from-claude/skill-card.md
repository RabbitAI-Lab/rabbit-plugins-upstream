## Description: <br>
Analyze Claude Usage and Cost JSON, show actual Anthropic spend in lattes, and estimate how many lattes the user could recover. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze Claude Platform Cost and Usage JSON exports locally, summarize spend, and identify directional cost recovery opportunities. The skill produces a short Claude Latte Report with cost groups, warnings, recovery basis, and a recovery estimate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Claude billing exports can contain sensitive spend, workspace, and usage data. <br>
Mitigation: Analyze only files explicitly provided by the user, keep analysis local, do not request API keys, and do not upload, retain, or reproduce raw billing data. <br>
Risk: The related external website is separate from the local analyzer and may handle user-entered information differently. <br>
Mitigation: Review the website before entering sensitive data, and keep the skill's billing-export analysis in the local script workflow. <br>
Risk: Recoverable cost is a directional estimate and may not translate into guaranteed savings. <br>
Mitigation: Present recovery as an estimate, state the recovery basis, and validate each optimization with a small production test before relying on it. <br>


## Reference(s): <br>
- [Supported input formats](references/input-formats.md) <br>
- [ClawHub skill page](https://clawhub.ai/margaretzybgl/skills/take-back-my-latte-from-claude) <br>
- [Take Back My Latte website](https://take-back-my-latte.margaret-zybgl.chatgpt.site) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report grounded in local JSON analyzer results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Under 250 words by default; includes a local-analysis privacy notice, warnings when present, cost breakdown, recoverable-cost estimate, and action link.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
