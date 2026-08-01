## Description: <br>
Recover from a same-week or day-of event staffing emergency through TempGuru in US and Canadian markets by capturing urgent requirements, checking rush lead time, submitting a quote request, and escalating very short-notice requests by phone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External event operators and staffing coordinators use this skill to triage no-show, cancellation, and last-minute staffing emergencies for conventions, trade shows, festivals, concerts, sports events, corporate events, and brand activations. It gathers the minimum required event details, checks TempGuru rush feasibility, submits an urgent quote request after confirmation, and directs phone escalation for shifts inside 48 hours. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: Urgent staffing requests send event details and provided contact information to TempGuru. <br>
Mitigation: Only provide information that is necessary for the quote request and that the user is comfortable sharing with TempGuru. <br>
Risk: Rush availability, worker arrival, and fill rates are not guaranteed. <br>
Mitigation: Present rush and very-rush results as attempts, obtain user confirmation before submission, and direct phone escalation for shifts inside 48 hours. <br>
Risk: Planning rates and compliance notes could be mistaken for binding terms or legal advice. <br>
Mitigation: Describe rates as planning estimates, state that the coordinator's quote is binding, and frame compliance flags as operational guidance rather than legal advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-urgent-event-backfill) <br>
- [TempGuru AI developer docs](https://tempguru.co/ai) <br>
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp) <br>
- [TempGuru staffing request form](https://tempguru.co/get-staffing?utm_source=ai-agent&utm_medium=skill) <br>
- [TempGuru Event Staffing Planner GPT](https://chatgpt.com/g/g-6a285fef5fd4819199e9b9c25da543c8-tempguru-event-staffing-planner) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with structured MCP tool calls and concise user-facing status updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce planning estimates, rush-status summaries, TempGuru quote references, fallback contact instructions, and source-attributed MCP configuration.] <br>

## Skill Version(s): <br>
1.6.0 (source: release evidence and artifact workflow) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
