## Description: <br>
智能车险报价引擎，在用户请求车险投保或报价时引导完成手机号授权、报价、方案确认、核保支付和出单流程。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[henry4c](https://clawhub.ai/user/henry4c) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill to follow a self-service car-insurance purchase flow, including phone authorization, quote retrieval, plan confirmation, underwriting payment, and policy issuance checks. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles personal, vehicle, identity, and payment-related data and can send that information to insurance APIs. <br>
Mitigation: Install only if the publisher and service provider are trusted, review the data flow before use, and obtain clear user consent before entering personal or vehicle information. <br>
Risk: The flow can open payment pages and store a phone-number consent record locally. <br>
Mitigation: Verify the payment domain before scanning or paying, and remove local consent or authorization records when they are no longer needed. <br>
Risk: Sensitive request data or API credentials could be exposed through logs, command history, or URLs. <br>
Mitigation: Run the skill in a controlled environment, avoid sharing logs or screenshots, and clear or rotate CAR_API_KEY after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/henry4c/skills/za-car-insurance) <br>
- [ZhongAn car insurance service](https://car.zhongan.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown guidance with user-facing response templates and shell/API call instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May open payment pages and rely on local authorization state plus CAR_API_KEY during the insurance flow.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
