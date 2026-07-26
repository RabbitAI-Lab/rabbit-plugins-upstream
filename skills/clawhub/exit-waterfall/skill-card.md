## Description: <br>
Compute who gets what at each exit price from a cap table, including liquidation preferences, conversion points, founder payout cliffs, and plain-English interpretations of the results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Founders, operators, investors, and advisors use this skill to model cap-table exit waterfalls, compare stakeholder payouts across exit prices, and identify where liquidation preferences, option strikes, and conversion decisions change outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process confidential cap-table and financing data. <br>
Mitigation: Use only data the agent is authorized to handle, avoid unnecessary disclosure of sensitive financing terms, and review generated outputs before sharing. <br>
Risk: Financial waterfall outputs can be misleading if the model assumptions do not match the company documents. <br>
Mitigation: Confirm liquidation seniority, participation caps, option treatment, and other legal terms against the source documents and consult a licensed professional before acting on the results. <br>
Risk: The skill references a helper script that is not included in the package. <br>
Mitigation: Only run scripts that exist in the local environment and come from a trusted source; otherwise perform or review the calculations without executing unknown code. <br>


## Reference(s): <br>
- [Exit Waterfall skill page](https://clawhub.ai/mohitagw15856/skills/exit-waterfall) <br>
- [Publisher profile](https://clawhub.ai/user/mohitagw15856) <br>
- [Project documentation](https://mohitagw15856.github.io/pm-claude-skills/skill/exit-waterfall.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown payout analysis with tables, assumptions, limitations, and optional shell commands for a deterministic helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes an educational-not-financial-advice disclaimer and names model simplifications such as pari passu preferences and uncapped participation.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
