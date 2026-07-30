## Description: <br>
This skill helps agents query Juhe Data's paid birth-chart service for calendar, zodiac, four-pillar, and five-elements details from a user's confirmed birth date and hour. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and consumer agents use this skill to request paid Chinese birth-chart lookup results through Juhe Data after reviewing the payment and privacy notice. It is intended for entertainment-style calendar and five-elements information, not for important medical, financial, legal, or life decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid Alipay-mediated service, so users could approve a charge without intending to buy the result. <br>
Mitigation: Review the payment prompt and fee before approving, and cancel if the paid lookup is not wanted. <br>
Risk: Each query sends the confirmed birth year, month, day, and hour to Juhe Data. <br>
Mitigation: Use the skill only when comfortable sharing those fields with the third-party service, and do not provide extra identity or contact information. <br>
Risk: Birth-chart and fortune-style outputs can be misleading if treated as factual advice. <br>
Mitigation: Treat results as entertainment and do not rely on them for medical, financial, legal, or other important decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-birth-eight-a2a) <br>
- [Publisher profile](https://clawhub.ai/user/juhemcp) <br>
- [Juhe Data A2A API endpoint](https://apis.juhe.cn/a2a/query) <br>
- [Output format documentation](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown responses with structured tables, payment-flow guidance, and occasional curl command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses only returned service fields for final birth-chart content and includes an entertainment-only disclaimer.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
