## Description: <br>
Book Piercing helps agents search for piercing services, check availability, and create bookings through Lokuli's MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and their agents use this skill to find piercing providers, check appointment availability, and book a selected piercing service through Lokuli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Booking creation sends customer contact details and appointment selections to Lokuli. <br>
Mitigation: Before calling create_booking, confirm the provider, service, date, time, customer name, email, and phone number, and avoid sharing unnecessary personal information. <br>


## Reference(s): <br>
- [Book Piercing ClawHub page](https://clawhub.ai/edwardrodriguez703-design/skills/book-piercing) <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls] <br>
**Output Format:** [Markdown with JSON-RPC tool-call arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Lokuli MCP tools for search, availability checks, and booking creation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
