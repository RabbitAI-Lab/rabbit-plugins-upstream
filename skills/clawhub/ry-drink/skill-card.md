## Description: <br>
瑞玥餐饮API helps an agent query restaurant shop, menu, table, reservation, member, transaction, order, and payment information through tools, and perform reservation and dining-order actions when appropriate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhimibuhui](https://clawhub.ai/user/zhimibuhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Restaurant customer-service agents use this skill to retrieve live restaurant data, manage table reservations, manage dining orders, and provide payment links for the intended tenant and shop. The skill is intended for customer-facing booking, ordering, and account-support workflows where tool results should be used instead of memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill for the wrong restaurant tenant or shop could direct queries or business actions to the wrong account. <br>
Mitigation: Install it only for the intended tenant/shop and verify that the platform injects the correct tenant, shop, SaaS, and phone context. <br>
Risk: Cancellation, order reduction, reservation changes, and payment-link generation can affect real restaurant operations. <br>
Mitigation: Require clear user confirmation before invoking business-write tools or payment-link tools. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhimibuhui/skills/ry-drink) <br>
- [Publisher Profile](https://clawhub.ai/user/zhimibuhui) <br>
- [Tool Schema](artifact/tools.json) <br>
- [Tool Router Notes](artifact/tool-router.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, configuration, guidance] <br>
**Output Format:** [JSON tool responses and concise Chinese plain-text business replies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses platform-supplied tenant, shop, SaaS, and phone context; write-capable tools can create, change, cancel, or reduce reservations and orders.] <br>

## Skill Version(s): <br>
1.0.31 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
