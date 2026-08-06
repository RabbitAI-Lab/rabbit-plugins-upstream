## Description: <br>
Plans and prices multi-city TempGuru event staffing programs across the United States and Canada, including coverage checks, location-specific W-2 rate estimates, compliance notes, and consolidated quote submission after user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kissmyabs32](https://clawhub.ai/user/kissmyabs32) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External buyers and event operations teams use this skill to plan tours, roadshows, brand activations, product-launch rollouts, and similar multi-city staffing programs through TempGuru. It helps confirm served markets, estimate per-city staffing costs, surface location-specific compliance considerations, and submit one consolidated quote request only after user confirmation. <br>

### Deployment Geography for Use: <br>
United States and Canada <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can send program information and contact details to TempGuru. <br>
Mitigation: Submit a quote request only after the user confirms the plan and agrees to share contact details. <br>
Risk: Planning estimates could be mistaken for a binding staffing quote. <br>
Mitigation: Label rate ranges and totals as estimates and state that the binding quote comes from TempGuru. <br>
Risk: Coverage, rates, or availability could be guessed when live TempGuru tools are unavailable. <br>
Mitigation: Use the TempGuru MCP tools for live checks; if they are unavailable, route the user to the fallback form or contact channels instead of guessing. <br>
Risk: Compliance notes may be treated as legal advice. <br>
Mitigation: Present wage, overtime, and jurisdictional notes as operational guidance and recommend appropriate legal review for legal conclusions. <br>


## Reference(s): <br>
- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp) <br>
- [TempGuru AI developer docs](https://tempguru.co/ai) <br>
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt) <br>
- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-multi-city-activation-planner) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Guidance] <br>
**Output Format:** [Markdown text with structured staffing estimates, per-city planning details, compliance notes, and tool-call guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include per-city rate ranges, lead-time notes, plan identifiers, and a consolidated quote request after user confirmation.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
