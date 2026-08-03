## Description: <br>
Helps agents query Juhe's paid birthday-oracle service for date-specific birthday book, birthday code, birthday flower, personality, luck, and related entertainment content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and consumer agents use this skill to request paid entertainment-style birthday information for a specific date after confirming an Alipay-based checkout flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a paid entertainment lookup that sends the requested date to Juhe and routes checkout through Alipay. <br>
Mitigation: Before payment, verify the displayed price, merchant, order number, and payment details, and continue only after explicit user confirmation. <br>
Risk: Birthday readings may be mistaken for factual, scientific, medical, career, or relationship advice. <br>
Mitigation: Present results as entertainment-only content and avoid using them as the basis for consequential decisions. <br>
Risk: Payment or query parameters could be altered during handoff. <br>
Mitigation: Preserve the original query date and payment response details when handing off to the Alipay payment skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-birthday-oracle-a2a) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>
- [Output format evidence](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Structured Markdown rendered from returned API fields, with payment handoff guidance when checkout is required] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the requested date as the query parameter; paid lookup requires user confirmation and Alipay payment-skill handoff.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
