## Description: <br>
zayn-shipment is a Chinese-language shipment notice workflow that checks post-dispatch details and drafts notices with carrier, tracking number, package count, weight, documents, and remaining quantities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations, order management, and delivery teams use this skill after goods have actually shipped to verify required shipment details and draft customer-facing shipment notifications. It is intended to stop or label preliminary analysis when carrier handoff, tracking, quantity, or remaining-shipment status is missing, conflicting, or unverified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shipment notices can include sensitive order numbers, tracking numbers, shipment documents, and recipient details. <br>
Mitigation: Treat these details as sensitive business data and review drafted notices before sending messages or changing source records. <br>
Risk: Incomplete or unverified logistics inputs can lead to premature shipment claims, invented tracking details, or ETA statements that sound guaranteed. <br>
Mitigation: Require confirmed carrier handoff, authentic tracking information, clear shipped quantity, and explicit remaining-quantity status before producing a final notice. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zaynpeng/skills/zayn-shipment) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style structured shipment notice analysis and draft text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a parameter completeness conclusion, parameter status table, shipment summary, attachment checklist, remaining-quantity status, risks and reminders, sendable draft, and follow-up checkpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
