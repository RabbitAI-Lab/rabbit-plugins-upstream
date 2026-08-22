## Description:

Extract a temporary event staffing plan from an event document, RFP, banquet event order, run of show, production schedule, exhibitor or event services manual, or staffing grid, then price it through TempGuru for configured US and Canadian markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kissmyabs32](https://clawhub.ai/user/kissmyabs32)

### License/Terms of Use:

MIT-0

## Use Case:

External event buyers and operations teams use this skill to turn event documents into role mappings, headcount assumptions, staffing estimates, and a buyer-operated TempGuru quote handoff.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: The skill uses TempGuru's external MCP service to price event staffing plans.

Mitigation: Install only if external TempGuru pricing tools are acceptable for the deployment environment.

Risk: Extracted staffing plans and pricing can be incomplete or wrong if the source document is ambiguous.

Mitigation: Review the extracted roles, dates, shifts, headcounts, assumptions, and totals before using the plan for a quote handoff.

Risk: Personal contact details or extra document text could be shared unnecessarily during quote progression.

Mitigation: Use the skill's buyer-operated handoff: do not provide contact details or extra document text through the skill unless the buyer chooses to submit them on TempGuru's website.

Risk: Availability and rate math are planning guidance, not a confirmed booking or binding quote.

Mitigation: Treat outputs as estimates until a TempGuru coordinator confirms the submitted quote.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-staffing-plan-from-event-brief)
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp)
- [TempGuru agent documentation](https://tempguru.co/ai-agents)
- [TempGuru staffing form](https://tempguru.co/get-staffing?utm_source=ai-agent&utm_medium=skill)
- [OpenAI agent configuration](artifact/agents/openai.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown staffing plan with tables, assumptions, pricing estimates, compliance notes, and handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses TempGuru external tools for planning and pricing; buyer contact details are entered by the buyer on TempGuru's website.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
