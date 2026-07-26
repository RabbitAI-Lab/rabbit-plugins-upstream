## Description: <br>
Credit card rewards optimizer that helps maximize cashback, points, and miles by recommending the best card for each purchase category, tracking annual caps, calculating annual fee ROI, managing rotating quarterly categories, and suggesting new cards based on spending patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scottfo](https://clawhub.ai/user/scottfo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to choose the best credit card for purchases, compare reward rates, track card reward caps, evaluate annual fee value, and plan card additions or removals from a local rewards profile. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may accidentally store sensitive financial data in the local card profile. <br>
Mitigation: Keep cards.json limited to card names, reward rules, activation status, and rough spending estimates; do not store card numbers, bank logins, statements, credentials, or detailed purchase records. <br>
Risk: Rotating category reminders or scheduled checks may run when the user does not expect automation. <br>
Mitigation: Enable quarterly reminder or cron automation only after the user explicitly requests it and knows how to disable it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scottfo/skills/card-optimizer) <br>
- [Skill homepage](https://github.com/ScotTFO/card-optimizer-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces recommendations, ROI summaries, gap analysis, and local cards.json configuration guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
