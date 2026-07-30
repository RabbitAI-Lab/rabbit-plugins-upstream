## Description: <br>
Provides a paid birthday-oracle lookup that uses a user-provided date to retrieve birthday-book, birthday-code, birthday-flower, personality, fortune, and related entertainment content from Juhe after Alipay payment confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to query entertainment-oriented birthday readings for a specific date, including birthday book, birthday code, birthday flower, personality, relationship, career, health, lucky information, tarot, and same-day celebrity sections. The skill requires user payment confirmation and a concrete date before it sends the date to Juhe. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may not understand the service is paid before providing a date or proceeding with payment. <br>
Mitigation: Require an explicit fee, Alipay payment, and privacy disclosure before collecting parameters or initiating the lookup. <br>
Risk: The skill sends a user-provided date to Juhe for the lookup. <br>
Mitigation: Send only the date required for the query, avoid collecting other personal information, and do not use the date for any other purpose. <br>
Risk: Entertainment readings could be mistaken for serious life, health, career, or relationship advice. <br>
Mitigation: Present results as entertainment-only content and include a clear notice that outputs are not scientifically grounded or suitable for major decisions. <br>
Risk: Payment flow or request parameters could be altered by the agent. <br>
Mitigation: Pass the full 402 payment response to the Alipay payment skill and keep the user-submitted request parameters unchanged. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-birthday-oracle-a2a) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Guidance] <br>
**Output Format:** [Structured Markdown with tables and sections rendered from the paid API response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Only uses returned interface fields, converts returned HTML to plain Markdown, and includes an entertainment-only disclaimer.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
