## Description: <br>
Run WhatsApp Business operations while protecting quality score with 24-hour windows, approved templates, and duplicate guards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations teams and developers use this skill to manage opt-in WhatsApp Business inbound replies, first-contact templates, and follow-ups through a BSP API while maintaining duplicate guards, recaps, and human handoff. <br>

### Deployment Geography for Use: <br>
Global, subject to WhatsApp Business requirements and local privacy obligations. <br>

## Known Risks and Mitigations: <br>
Risk: Lead personal data may be stored locally or sent to an alert channel. <br>
Mitigation: Confirm the alert destination is approved for lead names and phone numbers, use the documented retention windows, and honor deletion requests across every register. <br>
Risk: A broad or reused WhatsApp API token could expose more than the intended business number. <br>
Mitigation: Scope the API token to one WhatsApp business number and avoid full-account tokens. <br>
Risk: Unsolicited, duplicate, or closed-window messages can harm WhatsApp quality score or violate platform rules. <br>
Mitigation: Confirm opt-in before contact, check the 24-hour window before every free-form reply, and read duplicate registers before every outbound action. <br>
Risk: Privacy obligations vary by business domain and jurisdiction. <br>
Mitigation: For legal, medical, financial, or similarly sensitive use cases, confirm retention, alerting, and data minimization rules with the responsible privacy or legal reviewer before cron writes lead data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/whatsapp-business-ops) <br>
- [ClawHub metadata homepage](https://clawhub.ai/alexbloch-ia/whatsapp-business-ops) <br>
- [Whatchimp API base URL](https://app.whatchimp.com/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with YAML configuration examples, curl commands, local file conventions, and recap templates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl; no network call is available until placeholders such as API tokens, phone number IDs, and alert destinations are configured.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
