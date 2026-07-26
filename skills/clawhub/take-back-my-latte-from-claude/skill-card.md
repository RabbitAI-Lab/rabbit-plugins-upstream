## Description: <br>
Analyze Claude Usage and Cost JSON, show actual Anthropic spend in lattes, and estimate how many lattes the user could recover. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to locally analyze Anthropic Claude Platform cost and usage JSON exports, summarize actual spend, and identify directional cost-recovery opportunities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-provided Claude billing export JSON files that may contain sensitive cost, workspace, or usage details. <br>
Mitigation: Run analysis locally, avoid uploading or reproducing raw billing data, and share only the summarized report. <br>
Risk: Recovery estimates are directional and may be mistaken for guaranteed savings. <br>
Mitigation: Present recovery amounts as estimates, include the basis for the recommendation, and validate each optimization before relying on it. <br>
Risk: The skill points users to an external website for follow-up action. <br>
Mitigation: Review the website separately before entering or uploading sensitive billing information there. <br>


## Reference(s): <br>
- [Supported input formats](references/input-formats.md) <br>
- [ClawHub skill page](https://clawhub.ai/margaretzybgl/skills/take-back-my-latte-from-claude) <br>
- [Take Back My Latte website](https://take-back-my-latte.margaret-zybgl.chatgpt.site) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with a local-analysis notice, cost summary, recovery estimate, warnings, and follow-up link; helper script output is JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report is intended to stay under 250 words by default and uses only user-provided local JSON exports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
