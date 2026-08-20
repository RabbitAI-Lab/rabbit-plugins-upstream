## Description:

Helps users plan temporary W-2 event staffing through TempGuru, including requirements gathering, configured-market matching, rate and compliance lookups, and a buyer-operated quote-form handoff for US and Canadian events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kissmyabs32](https://clawhub.ai/user/kissmyabs32)

### License/Terms of Use:

MIT-0

## Use Case:

External event buyers and planners use this skill to turn event details into a reviewed TempGuru staffing plan with role counts, rate ranges, lead-time guidance, compliance notes, and a buyer-operated quote handoff. It is intended for temporary event staffing requests in the United States and Canada, not permanent hiring or events outside those countries.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: Generated staffing plans, pricing, and availability guidance may be mistaken for confirmed order terms.

Mitigation: Review the generated plan before using the handoff and treat pricing and availability as estimates until TempGuru confirms them.

Risk: Users may include sensitive event information in a saved staffing plan snapshot.

Mitigation: Avoid adding sensitive event details that should not be stored in the 30-day non-PII plan snapshot.

Risk: Users may expect the handoff to submit contact details or create an order automatically.

Mitigation: Use the quote handoff as a buyer-operated form flow; the buyer reviews the plan and submits their own contact details on TempGuru's form.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-event-staffing-ordering)
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp)
- [TempGuru staffing request form](https://tempguru.co/get-staffing?utm_source=ai-agent&utm_medium=skill)
- [TempGuru machine-readable site overview](https://tempguru.co/llms.txt)
- [TempGuru Event Staffing Planner GPT](https://chatgpt.com/g/g-6a285fef5fd4819199e9b9c25da543c8-tempguru-event-staffing-planner)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown with structured staffing plan summaries, estimated rate ranges, operational notes, and quote handoff URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses TempGuru planning, pricing, policy, compliance, and handoff tools; generated plans should be reviewed before use and do not submit buyer contact details.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
