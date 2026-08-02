## Description: <br>
This skill provides paid birth-chart lookup using Juhe Data's API to return lunar calendar, zodiac, stems-and-branches, eight-character, and five-elements information from a confirmed Gregorian birth date and hour. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to request a paid entertainment-style birth-chart report after confirming the birth year, month, day, and hour. The skill formats the API response as a Markdown report and should not be used for medical, financial, legal, career, or other consequential decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends birth date and birth hour to a third-party API for a paid lookup. <br>
Mitigation: Use the skill only after reviewing and accepting the payment and privacy prompt; cancel if sharing those details is not acceptable. <br>
Risk: Birth-chart and five-elements output may be mistaken for decision guidance. <br>
Mitigation: Treat the report as entertainment only and do not rely on it for medical, financial, legal, career, relationship, or other consequential decisions. <br>
Risk: The paid workflow depends on Alipay payment handling and a 402 payment response. <br>
Mitigation: Confirm the order details, amount, and payment method before payment, and avoid proceeding if the payment prompt is incomplete or unexpected. <br>
Risk: Incomplete or incorrect birth parameters can produce incorrect lookup results. <br>
Mitigation: Provide and verify the Gregorian year, month, day, and hour before the API request is made. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-birth-eight-a2a) <br>
- [Juhe birth-chart API endpoint](https://apis.juhe.cn/a2a/query) <br>
- [Output format artifact](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with tables after a paid API response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses only the API response fields and the user-confirmed birth year, month, day, and hour; includes an entertainment-only disclaimer.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
