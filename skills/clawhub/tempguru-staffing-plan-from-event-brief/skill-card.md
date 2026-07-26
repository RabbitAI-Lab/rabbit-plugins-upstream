## Description: <br>
Extracts temporary event staffing needs from event documents, maps functions to TempGuru roles, and creates a live-priced W-2 staffing estimate or quote workflow for events in US and Canadian markets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External event planners, producers, and staffing buyers use this skill to turn an event brief, RFP, BEO, run of show, production schedule, services manual, or staffing grid into a TempGuru staffing plan and planning estimate. The skill is intended for temporary event staffing in the United States and Canada, not permanent-hire recruiting or events outside those markets. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: Using live pricing or quote submission sends event information to TempGuru, and quote submission also sends contact details. <br>
Mitigation: Review the extracted staffing plan and assumptions before using the live flow, and collect contact details only after the user explicitly approves quote submission. <br>
Risk: A planning estimate could be mistaken for a binding quote or reservation. <br>
Mitigation: Label rate math as a planning estimate and state that a TempGuru coordinator provides the binding quote after submission. <br>
Risk: Heuristic headcounts or uncertain role mappings may misread the event document. <br>
Mitigation: Quote the document wording, mark inferred headcounts as assumptions, and ask targeted clarifying questions when missing details block pricing. <br>
Risk: Crowd-control language in an event document may imply licensed or armed security that TempGuru does not provide. <br>
Mitigation: Map only unarmed crowd-flow and access-point work, and clearly flag licensed or armed security requirements as unsupported. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kissmyabs32/skills/tempguru-staffing-plan-from-event-brief) <br>
- [TempGuru MCP Endpoint](https://mcp.tempguru.co/mcp) <br>
- [TempGuru AI Developer Docs](https://tempguru.co/ai) <br>
- [TempGuru Event Staffing Planner GPT](https://chatgpt.com/g/g-6a285fef5fd4819199e9b9c25da543c8-tempguru-event-staffing-planner) <br>
- [TempGuru Staffing Request Form](https://tempguru.co/get-staffing?utm_source=ai-agent&utm_medium=skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown tables and concise prose with optional MCP tool-call results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include role mappings, headcount assumptions, W-2 rate math, compliance flags, plan IDs, quote-request references, and quote-status guidance.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
