## Description: <br>
瑞玥餐饮API2 helps restaurant agents retrieve live shop, menu, table, appointment, member, transaction, order, and payment-link data and perform reservation or order changes through configured tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhimibuhui](https://clawhub.ai/user/zhimibuhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External diners and restaurant staff use this skill to answer restaurant service questions with live backend data and to complete bookings, order changes, cancellations, and payment-link requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access customer, member, appointment, order, and transaction data. <br>
Mitigation: Install only in the intended merchant environment and confirm backend authorization, session-phone binding, and tenant/shop isolation before use. <br>
Risk: The skill can change reservations and dining orders or create payment links. <br>
Mitigation: Require explicit user confirmation before cancellations, order changes, and payment-link generation. <br>
Risk: Phone and member identifiers may be sent to backend services. <br>
Mitigation: Verify what phone and member data is transmitted and limit deployment to approved merchant sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhimibuhui/skills/ry-drink2) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, guidance] <br>
**Output Format:** [Chinese user-facing text with backend tool results rewritten into business responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return payment URLs and customer/order summaries; internal tool names, order IDs, reservation IDs, and diagnostic details are intended to be withheld from end users.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact/skill.json reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
