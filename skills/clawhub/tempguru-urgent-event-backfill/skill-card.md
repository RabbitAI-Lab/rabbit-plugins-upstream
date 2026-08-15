## Description:

Recover from a same-week or day-of event staffing emergency through TempGuru using configured US and Canadian markets, rush lead-time guidance, a buyer-operated quote-form handoff, and honest no-show backfill framing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kissmyabs32](https://clawhub.ai/user/kissmyabs32)

### License/Terms of Use:

MIT-0

## Use Case:

External buyers and event operators use this skill to triage last-minute event staffing shortfalls, gather the minimum operational details, check TempGuru rush guidance, and prepare a buyer-controlled quote handoff. It is intended for conventions, trade shows, festivals, concerts, sporting events, corporate events, and brand activations in the United States and Canada.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: Operational event details are sent to TempGuru tools and channels.

Mitigation: Collect only the staffing details needed for planning, avoid contact details in the MCP handoff, and have the buyer submit their own contact information on TempGuru-owned channels.

Risk: Rush staffing guidance can be mistaken for guaranteed coverage.

Mitigation: State that rush and very-rush requests are attempts, not guarantees, and direct the buyer to complete the form and call TempGuru for starts inside 48 hours.

Risk: A no-show by another vendor or gig app can be misclassified as TempGuru contractual backfill.

Mitigation: Distinguish TempGuru placement no-shows from new rush orders and use TempGuru policy guidance before explaining replacement commitments.

Risk: The user may request licensed or armed security outside the skill's service scope.

Mitigation: Clarify that TempGuru's security category means unarmed crowd-control staffing and does not cover licensed or armed security.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-urgent-event-backfill)
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp)
- [TempGuru AI Agents developer docs](https://tempguru.co/ai-agents)
- [TempGuru staffing form](https://tempguru.co/get-staffing?utm_source=ai-agent&utm_medium=skill)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API Calls, Configuration]

**Output Format:** [Markdown guidance with MCP tool call instructions and buyer handoff links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill provides planning estimates and handoff guidance; the binding quote and order coverage must be confirmed by TempGuru.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
