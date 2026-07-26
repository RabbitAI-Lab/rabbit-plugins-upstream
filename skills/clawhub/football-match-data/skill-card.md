## Description: <br>
Generates paid football match data reports by collecting and cross-checking public fixture, team, player-status, standings, form, and odds-related data from multiple sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wht0202](https://clawhub.ai/user/wht0202) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and football analysts use this skill to request a paid, standardized football match data report for a specified fixture after order creation and payment processing. The report is intended for sports data analysis and review, not as automated wagering execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is security-classified as suspicious because it combines paid football-data reporting with under-disclosed betting-analysis behavior. <br>
Mitigation: Review the skill before installation and require clear user-facing disclosure that outputs may include betting-analysis context and are not financial or wagering advice. <br>
Risk: The skill requests payment processing, credential access, and outbound network access while handling local order and payment state. <br>
Mitigation: Run it with least-privilege credentials in an isolated environment and verify payment/order storage behavior before production use. <br>
Risk: The security summary reports runtime code writes and exposed credentials. <br>
Mitigation: Remove exposed credentials, disable runtime source modification, and scan the artifact again before deployment. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/wht0202/skills/football-match-data) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Project README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with text status fields and tabular football match data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require network access, payment processing, credential access, and a valid order number before report generation.] <br>

## Skill Version(s): <br>
2.9.2 (source: SKILL.md frontmatter and server release metadata; pyproject.toml reports 2.7.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
