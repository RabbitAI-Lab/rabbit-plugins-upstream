## Description: <br>
Send email, SMS, and voice calls from your agent after configuring the Hail API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hail-hq](https://clawhub.ai/user/hail-hq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use Hail Communication to send email, SMS, and voice calls through the Hail API. The skill is intended for consent-based outbound communication where the operator has configured HAIL_API_KEY and confirmed a lawful basis to contact each recipient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to send real email, SMS, or voice calls through Hail. <br>
Mitigation: Authorize sends only for intended recipients and require human approval where real-world communication could have legal, financial, or reputational impact. <br>
Risk: HAIL_API_KEY grants access to the Hail account and is shown only once during signup. <br>
Mitigation: Store HAIL_API_KEY in a secret manager or protected environment variable and never paste it into chat, logs, or public files. <br>
Risk: Outbound communication may violate consent, anti-spam, or telemarketing rules if used without a lawful basis. <br>
Mitigation: Send only when recipient_consent is true, record the consent source for marketing messages, and follow applicable TCPA, ePrivacy, PECR, CAN-SPAM, and GDPR obligations. <br>
Risk: Agent signup can accept Hail's terms on the human owner's behalf. <br>
Mitigation: Confirm the owner agrees to Hail's terms before setting tou_accepted during signup. <br>
Risk: Repeated requests may hit Hail rate limits or exhaust free credit. <br>
Mitigation: Back off on 429 responses, respect retry timing, and ask the owner to top up through the claim URL after a 402 response. <br>


## Reference(s): <br>
- [Hail API documentation](https://docs.hail.so) <br>
- [Hail pricing](https://hail.so/pricing) <br>
- [ClawHub skill page](https://clawhub.ai/hail-hq/skills/hail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HAIL_API_KEY and explicit recipient consent for sends.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
