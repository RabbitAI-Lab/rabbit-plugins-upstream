## Description: <br>
输入航班号自动查延误状态并计算权益金额，覆盖欧盟、英国、中国、加拿大、美国和土耳其6大法域，并生成权益申领指引和申领信。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-support agents use this skill to check flight delay status, compare passenger-rights rules across supported jurisdictions, estimate compensation eligibility, and draft a claim letter for airline submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Flight numbers and dates are sent off-device to the listed cloud proxy/flight-data service. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid entering unnecessary personal details. <br>
Risk: The passenger name may appear in the generated claim-letter template. <br>
Mitigation: Provide only the minimum personal information needed for the letter and review the generated text before sending it to an airline. <br>
Risk: The artifact includes an embedded fallback proxy token. <br>
Mitigation: Publisher should replace the fallback token with a properly scoped managed secret before broader deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/flight-delay-compensation) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown and plain-text guidance with inline claim-letter templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses flight number, travel date, optional region, and optional passenger name; flight lookups are sent through the listed cloud proxy/flight-data service.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
