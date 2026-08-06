## Description: <br>
Extracts temporary event staffing plans from event documents, maps event functions to TempGuru roles, prices the plan through TempGuru, and supports quote submission after user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Event planners, venue teams, and operations staff use this skill to extract staffing needs from RFPs, banquet event orders, schedules, manuals, and staffing grids, then produce a priced temporary staffing plan for US and Canadian events. The skill is intended for event staffing budgets and quote workflows, not permanent hiring documents. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: Event logistics such as city, venue, dates, shifts, roles, and headcounts may be sent to TempGuru for pricing. <br>
Mitigation: Install and use the skill only when sharing those event logistics with TempGuru is acceptable. <br>
Risk: A quote workflow may require contact details and could be mistaken for a final booking step. <br>
Mitigation: Review the staffing plan first and submit a quote only after explicit user confirmation and readiness to provide contact details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-staffing-plan-from-event-brief) <br>
- [TempGuru AI developer docs](https://tempguru.co/ai) <br>
- [TempGuru staffing request form](https://tempguru.co/get-staffing?utm_source=ai-agent&utm_medium=skill) <br>
- [TempGuru Event Staffing Planner GPT](https://chatgpt.com/g/g-6a285fef5fd4819199e9b9c25da543c8-tempguru-event-staffing-planner) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown plan with staffing tables, estimates, assumptions, compliance notes, and quote handoff details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include TempGuru plan identifiers, continuation URLs, or quote reference IDs when the user requests saving or quote submission.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
