## Description: <br>
Maejongdeok helps users view clinic information, submit booking requests, consult support, and query prices for 梅宗德医院 through BeautsGO. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beautsgo](https://clawhub.ai/user/beautsgo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to navigate BeautsGO booking flows for 梅宗德医院, including viewing appointment guidance, submitting appointment requests, opening consultation pages, and checking project prices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking details and any phone number the user provides may be sent to BeautsGO/Yestokr, and price queries use another external API. <br>
Mitigation: Install and use the skill only when that external data sharing is acceptable, and clearly disclose it to users before collection. <br>
Risk: The security evidence notes that appointment details can be submitted without a clear final consent step. <br>
Mitigation: Require an explicit final user confirmation before submitting a booking request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/beautsgo/maejongdeok-clinic-booking) <br>
- [Maejongdeok clinic booking page](https://i.beautsgo.com/cn/hospital/maisondem-clinic/skill) <br>
- [BeautsGO website](https://www.beautsgo.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown-formatted string] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include booking status, price results, external links, or next-step instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, skill.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
