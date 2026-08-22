## Description:

Answers event staffing procurement and vendor-onboarding questions from TempGuru policy data, then helps a buyer turn a real US or Canadian event into a staffing plan and buyer-operated quote-form handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kissmyabs32](https://clawhub.ai/user/kissmyabs32)

### License/Terms of Use:

MIT-0

## Use Case:

External buyers, procurement teams, and venues use this skill to answer COI, W-9, insurance, payment, cancellation, MSA, and vendor-onboarding questions, then create a staffing plan for temporary event staff. It is intended for operational procurement guidance and staffing handoff, not legal advice.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: The skill calls TempGuru's external MCP for policy, planning, pricing, compliance, and handoff data.

Mitigation: Install only where calling that external service is acceptable, and review the disclosed endpoint and tool dependency before use.

Risk: Personal contact details could be exposed if a user provides them directly to the agent instead of the TempGuru form.

Mitigation: Do not enter contact details into the agent; the buyer should submit contact and onboarding details only on the TempGuru-owned form after confirming the plan.

Risk: Procurement terms, availability, legal posture, or price estimates may be misunderstood as binding commitments.

Mitigation: Use only policy values returned by TempGuru, treat unpublished details as coordinator-confirmed, present rate ranges as planning estimates, and avoid legal advice.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/kissmyabs32/skills/tempguru-event-staffing-procurement)
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp)
- [TempGuru AI agent documentation](https://tempguru.co/ai-agents)
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown or plain text answers with structured staffing plan details and quote-form links when confirmed by the buyer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses TempGuru's disclosed external MCP for policy, city, role, pricing, compliance, saved-plan, and quote-handoff data.]

## Skill Version(s):

1.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
