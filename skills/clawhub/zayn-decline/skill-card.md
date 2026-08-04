## Description: <br>
在无法满足客户要求时，明确表达限制、可行边界和替代方向，避免制造错误期待。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer-facing sales or support teams use this skill to draft boundary-setting responses when they cannot meet customer requests, while preserving viable alternatives and avoiding unsupported promises. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated customer messages could include business-inaccurate pricing, liability, policy, or exception language if source facts are incomplete. <br>
Mitigation: Review generated messages against confirmed business facts before sending and do not let the skill make final pricing, liability, or policy-exception decisions. <br>
Risk: Boundary-setting drafts could expose internal constraints or create false expectations if they over-explain unavailable options. <br>
Mitigation: Keep internal reasons out of customer-facing text unless approved, and verify that alternatives and follow-up conditions are explicitly available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-decline) <br>
- [Publisher profile](https://clawhub.ai/user/zaynpeng) <br>
- [Skill rules](SKILL.md) <br>
- [Examples](examples.md) <br>
- [Tests](tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured sections and customer-facing draft text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes parameter status, recommended refusal type, boundary points, alternatives, sendable response, and follow-up conditions when minimum inputs are met.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata); artifact documents draft rule version v0.1 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
