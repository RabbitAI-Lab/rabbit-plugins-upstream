## Description: <br>
Recover from a same-week or day-of event staffing emergency through TempGuru in 345 US and Canadian markets by capturing urgent staffing requirements, checking rush lead time, and submitting a quote request after explicit confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External event operators and staffing coordinators use this skill when staff no-show, a vendor cancels, or an event within roughly 72 hours needs emergency staffing. It guides the agent through one-pass requirement capture, rush classification, explicit confirmation, urgent quote submission, and appropriate no-guarantee framing. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may send event details and contact information to TempGuru through MCP tools. <br>
Mitigation: Tell the user what will be submitted and require explicit confirmation before calling request_quote. <br>
Risk: Urgent staffing requests can be mistaken for guaranteed coverage. <br>
Mitigation: Frame rush and very-rush requests as attempts, not guarantees, and preserve the instruction to call TempGuru immediately for starts within 48 hours. <br>
Risk: Users may request licensed or armed security that TempGuru does not provide through this workflow. <br>
Mitigation: State that TempGuru provides unarmed crowd-control event staff only and redirect licensed or armed security needs. <br>


## Reference(s): <br>
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp) <br>
- [TempGuru AI developer docs](https://tempguru.co/ai) <br>
- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-urgent-event-backfill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, API Calls] <br>
**Output Format:** [Markdown or plain text with MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Collects event details and contact information, requires explicit confirmation before quote submission, and returns a TempGuru reference when submission succeeds.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
