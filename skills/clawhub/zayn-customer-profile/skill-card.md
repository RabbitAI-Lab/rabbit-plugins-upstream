## Description: <br>
Organizes traceable customer facts and information gaps from orders, inquiries, payments, shipments, after-sales records, communications, and public sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and customer-management teams use this skill to build evidence-based customer profiles from real business records and public information, while separating confirmed facts, conflicts, gaps, and unverified claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive customer records, including orders, payments, emails, chats, and after-sales history. <br>
Mitigation: Provide only the minimum customer data needed, redact payment details and unnecessary personal identifiers, and follow company privacy and retention rules. <br>
Risk: Public website or LinkedIn information could be mistaken for stronger evidence than real business records. <br>
Mitigation: Keep public sources auxiliary, preserve source labels, and prioritize transaction, inquiry, payment, shipment, after-sales, and confirmed communication records. <br>
Risk: Incomplete or conflicting records could lead to overconfident customer profiles. <br>
Mitigation: Mark missing, conflicting, or unverified items explicitly and avoid customer value judgments, segmentation, follow-up decisions, or deal probability estimates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-customer-profile) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>
- [Changelog](artifact/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown customer profile with evidence sections, information gaps, and downstream skill inputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Separates confirmed facts, evidence-supported judgments, conflicts, unverified information, and AI speculation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
