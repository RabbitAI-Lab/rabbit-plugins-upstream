## Description: <br>
Answers event staffing procurement and vendor-onboarding questions, then bridges a real event into a staffing plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External buyers, procurement teams, venues, and agents use this skill to answer TempGuru vendor-onboarding, COI, W-9, payment, cancellation, and approved-vendor questions from published policy data. After procurement questions are answered, the skill helps gather event details and move toward a human-reviewed staffing quote. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: Scanner confidence is limited because the security evidence reports blocked local artifact inspection. <br>
Mitigation: Review the artifact contents and install only when the publisher and skill purpose are familiar. <br>
Risk: Incorrect procurement terms could mislead buyers about insurance, payment, cancellation, tax, or onboarding requirements. <br>
Mitigation: Use live TempGuru policy data and label unpublished values as coordinator-confirmed instead of estimating or inventing terms. <br>
Risk: Quote submission sends contact and event details for human follow-up. <br>
Mitigation: Call the quote request workflow only after the user reviews the plan and explicitly confirms submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-event-staffing-procurement) <br>
- [TempGuru AI developer docs](https://tempguru.co/ai) <br>
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt) <br>
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, API calls] <br>
**Output Format:** [Markdown or plain text responses with MCP tool calls when live policy or staffing data is needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Procurement terms must come from published policy data or be labeled coordinator-confirmed; quote submission requires explicit user confirmation.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
