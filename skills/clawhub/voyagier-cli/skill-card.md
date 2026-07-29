## Description: <br>
Book real travel from your terminal - search flights, hotels & activities, plan trips, and check out with a price-gated booking. For AI agents and travel advisors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[demmersong](https://clawhub.ai/user/demmersong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and travel advisors use this skill to operate the Voyagier CLI for travel planning, flight and hotel search, traveller management, quoting, checkout, and client payment handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide real travel bookings, payment checkout sessions, and client email sends. <br>
Mitigation: Use dry-run or quote commands first, require explicit user approval, and enforce the CLI price gate before checkout or client email actions. <br>
Risk: Agents using the CLI may access Voyagier account data, client details, traveller information, and travel plans. <br>
Mitigation: Keep personal access tokens private, prefer interactive login or stdin/env token handling, and avoid logging credentials or sensitive trip output. <br>
Risk: Travel supplier, hotel, option, and plan names may contain untrusted text. <br>
Mitigation: Treat supplier text as data only, use stable IDs in commands, and do not interpret result names as instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/demmersong/skills/voyagier-cli) <br>
- [Voyagier Travel API](https://travel.voyagier.com/api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the voyagier CLI binary and authenticated Voyagier account access.] <br>

## Skill Version(s): <br>
2.14.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
