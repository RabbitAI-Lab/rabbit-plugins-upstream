## Description:

Plan and price a multi-city event staffing program with one consolidated TempGuru quote handoff across supported US and Canadian markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kissmyabs32](https://clawhub.ai/user/kissmyabs32)

### License/Terms of Use:

MIT-0

## Use Case:

External buyers and event staffing coordinators use this skill to estimate multi-city tours, roadshows, sampling programs, festival circuits, and brand activations before reviewing and submitting one TempGuru-owned quote form themselves.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: The skill contacts TempGuru's external MCP service for live planning data and may save one staffing-plan leg for form handoff.

Mitigation: Review the returned plan and form URL before use, and do not treat MCP planning output as a confirmed booking or binding quote.

Risk: Automatic quote lead creation or contact-detail submission would exceed the intended workflow.

Mitigation: Use the handoff as read-only: the buyer opens the TempGuru-owned form, verifies the full multi-city itinerary, enters their own contact details, and submits personally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-multi-city-activation-planner)
- [TempGuru AI agent documentation](https://tempguru.co/ai-agents)
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt)
- [TempGuru staffing form](https://tempguru.co/get-staffing?utm_source=ai-agent&utm_medium=skill)
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API Calls]

**Output Format:** [Markdown planning summary with per-city estimates, lead-time notes, compliance flags, and a buyer-operated form URL when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning estimates only; buyer must review the TempGuru form before submitting contact details.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
