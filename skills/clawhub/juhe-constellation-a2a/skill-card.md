## Description: <br>
Provides paid constellation profile and horoscope lookups for the twelve zodiac signs across daily, weekly, monthly, and yearly periods using Juhe's constellation service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to request paid constellation profiles and horoscope readings for a specified sign and period. Agent operators use it when a user explicitly requests horoscope content and accepts the payment and privacy disclosure flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a paid lookup flow and sends the selected zodiac sign and period to Juhe after confirmation. <br>
Mitigation: Show the payment and privacy disclosure before collection or request execution, and verify the payment amount before confirming each purchase. <br>
Risk: Horoscope and constellation content may be mistaken for factual, medical, financial, legal, or life-planning advice. <br>
Mitigation: Present results as entertainment only and avoid using them as the basis for important decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-constellation-a2a) <br>
- [Juhe constellation query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown horoscope and constellation profile output, with a fixed HTTPS API request during execution.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit payment confirmation; results are entertainment content and should not be treated as professional advice.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
