## Description: <br>
Plan and request temporary W-2 event staffing for US and Canadian events through TempGuru, including requirement gathering, live pricing and compliance lookups, planning estimates, and quote submission after user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and event planners use this skill to estimate staffing needs, review TempGuru coverage, rates, lead time, and operational compliance notes, and submit a human-reviewed quote request only after confirming the staffing plan. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: Planning and pricing depend on TempGuru's external MCP service. <br>
Mitigation: Install only when use of the TempGuru service is acceptable, and use the documented fallback form or contact channels if MCP access is unavailable. <br>
Risk: A quote request sends contact and event details to TempGuru for human follow-up. <br>
Mitigation: Submit a quote only after the user explicitly confirms the staffing plan and agrees to share those details. <br>
Risk: Planner persistence may create a temporary non-PII plan record. <br>
Mitigation: Use saved plan IDs only when resuming or sharing a plan is useful, and avoid including contact details until the quote request step. <br>
Risk: Rates and availability guidance are planning estimates, not binding quotes or reservations. <br>
Mitigation: Label estimates clearly and rely on TempGuru's human-reviewed quote before treating pricing or staffing availability as final. <br>


## Reference(s): <br>
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp) <br>
- [TempGuru staffing request form](https://tempguru.co/get-staffing?utm_source=ai-agent&utm_medium=skill) <br>
- [TempGuru machine-readable site overview](https://tempguru.co/llms.txt) <br>
- [TempGuru Event Staffing Planner GPT](https://chatgpt.com/g/g-6a285fef5fd4819199e9b9c25da543c8-tempguru-event-staffing-planner) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and structured planning guidance with MCP tool calls where supported] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce non-binding staffing estimates, plan IDs for 30-day non-PII plan retrieval, and quote request confirmations after explicit user approval.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
