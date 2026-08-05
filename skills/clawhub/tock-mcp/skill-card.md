## Description: <br>
Discover restaurants on Tock via MCP, including metros, venue details, bookable experiences, prices, party sizes, open dates and times, and signed-in account reservation lookups when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent look up Tock restaurant discovery, availability, reservation history, and profile information through the user's Tock browsing session. Booking, payment, and cancellation remain outside the skill and under the user's direct control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Signed-in account tools may expose Tock reservation history and profile details such as name and email to the agent. <br>
Mitigation: Install and use the skill only when that account visibility is acceptable, and call signed-in account tools only for the intended Tock lookup purpose. <br>
Risk: Prepaid booking, cancellation, and payment actions can create financial or reservation consequences if delegated incorrectly. <br>
Mitigation: Keep booking, cancellation, and payment steps on Tock under direct user control; use the skill for lookup and verification rather than making changes. <br>
Risk: Booking status can be misread if a confirmation screen appears but the reservation is not visible in a later account lookup. <br>
Mitigation: Treat a booking as confirmed only when a confirmation artifact is captured and `tock_list_reservations` shows the reservation after re-querying. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall) <br>
- [npm package](https://www.npmjs.com/package/tock-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Structured MCP tool responses with Markdown setup and usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on Tock page state, browser sign-in state, and the user's approved fetchproxy pairing.] <br>

## Skill Version(s): <br>
0.2.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
