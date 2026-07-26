## Description: <br>
Book towing services through Lokuli MCP for users who need to find and book towing services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardrodriguez703-design](https://clawhub.ai/user/edwardrodriguez703-design) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to search for towing providers, check service availability, and create a towing booking through Lokuli's MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating a booking shares the user's name, email, and phone number with Lokuli for towing service fulfillment. <br>
Mitigation: Confirm the user wants to share these contact details before calling create_booking. <br>
Risk: A towing booking may depend on provider, time slot, price, or cancellation terms that are not guaranteed by the skill text. <br>
Mitigation: Confirm the provider, appointment time, and any available price or cancellation details before completing the booking. <br>


## Reference(s): <br>
- [Lokuli MCP endpoint](https://lokuli.com/mcp/sse) <br>
- [ClawHub skill page](https://clawhub.ai/edwardrodriguez703-design/skills/book-towing) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with JSON-RPC MCP tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include towing search terms, ZIP code, provider and service identifiers, appointment time slots, and customer contact details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
