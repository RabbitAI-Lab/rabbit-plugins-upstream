## Description: <br>
Answers event staffing procurement and vendor-onboarding questions from TempGuru policy, then helps turn a confirmed US or Canadian event into a staffing plan and quote handoff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External buyers, procurement teams, venues, and agents use this skill to answer COI, W-9, insurance, payment, invoicing, MSA, and approved-vendor questions from TempGuru published policy before building a temporary event staffing plan. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: Event planning details are sent to TempGuru's external MCP service during policy, coverage, pricing, and staffing-plan workflows. <br>
Mitigation: Install only when that service use is acceptable for the intended event-planning workflow. <br>
Risk: Contact information may be submitted to TempGuru during quote handoff. <br>
Mitigation: The skill requires explicit user confirmation before calling the quote-request tool with contact details. <br>
Risk: Procurement terms such as COI limits, payment terms, cancellation windows, tax IDs, and MSA clauses could be misleading if invented. <br>
Mitigation: The artifact instructs agents to use published policy data or state that a TempGuru coordinator confirms unavailable values during onboarding. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-event-staffing-procurement) <br>
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp) <br>
- [TempGuru AI developer docs](https://tempguru.co/ai) <br>
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown or plain text responses with MCP tool calls when live policy, planning, or quote handoff data is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce non-binding staffing estimates and request explicit confirmation before quote submission] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
