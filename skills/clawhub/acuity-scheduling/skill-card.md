## Description: <br>
Acuity Scheduling API integration with managed OAuth for managing appointments, calendars, clients, and availability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an Acuity Scheduling account through Maton and perform scheduling workflows such as checking availability, booking, rescheduling, canceling appointments, and managing clients or calendars. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, cancel, or delete appointments, clients, blocks, and connections in a connected Acuity Scheduling account. <br>
Mitigation: Before approving write operations, confirm the exact account, resource, and intended effect with the user. <br>
Risk: Requests could affect the wrong Acuity Scheduling account when multiple connections are available. <br>
Mitigation: Use the Maton-Connection header to target the intended connection whenever more than one account is connected. <br>
Risk: The skill requires a Maton API key and access to scheduling and client data. <br>
Mitigation: Install only if you trust Maton, keep MATON_API_KEY protected, and limit use to the intended connected account. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/acuity-scheduling) <br>
- [Acuity Scheduling API Quick Start](https://developers.acuityscheduling.com/reference/quick-start) <br>
- [Appointments API](https://developers.acuityscheduling.com/reference/get-appointments) <br>
- [Availability API](https://developers.acuityscheduling.com/reference/get-availability-dates) <br>
- [Calendars API](https://developers.acuityscheduling.com/reference/get-calendars) <br>
- [Clients API](https://developers.acuityscheduling.com/reference/clients) <br>
- [OAuth2 Documentation](https://developers.acuityscheduling.com/docs/oauth2) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown with HTTP endpoints, Python and JavaScript examples, and shell configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an authorized Acuity Scheduling connection; use the Maton-Connection header when multiple accounts are connected.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
