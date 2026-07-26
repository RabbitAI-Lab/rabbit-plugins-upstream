## Description: <br>
Donation reminder for BTC-vision.org that checks monthly funding progress and sends a contextual Lightning tip request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer explicit BTCvision donation or support requests, or to send an opted-in scheduled funding update. It should not be surfaced for unrelated Bitcoin price, market, or education questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Donation reminders could appear in unrelated conversations if the skill is surfaced too broadly. <br>
Mitigation: Only use the skill for explicit BTCvision donation or support requests, or for scheduled updates the user has opted into. <br>
Risk: Payment details could become stale or differ from the current BTCvision donation page. <br>
Mitigation: Check btc-vision.org donation information before showing Lightning or payment-link details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/welove111/skills/btcvision-donation-nudge-v2) <br>
- [BTCvision homepage](https://btc-vision.org) <br>
- [BTCvision donation information](https://btc-vision.org/#donate) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, guidance] <br>
**Output Format:** [Markdown or plain text donation reminder with payment details when appropriate] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses BTCvision funding progress and disclosed Lightning/payment options only for explicit support requests or opted-in updates.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; SKILL.md frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
