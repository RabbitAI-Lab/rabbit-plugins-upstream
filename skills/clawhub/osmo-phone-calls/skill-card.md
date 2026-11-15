## Description:

Phone call AI: make phone calls with AI. AI phone call skill: use when the user wants an AI to make a real phone call for them — call a business, shop, clinic, restaurant, helpline or a person they know; book, reschedule or cancel an appointment or reservation; reach customer service and get through the phone menu; ask a question and bring back the answer with a summary. Also use to see who called the user's OsmO number, what they wanted, and to change OsmO call screening rules. Free to start in the US, Canada, UK and Australia, where free credits call businesses and toll-free numbers; calling contacts and scheduling need an OsmO app plan. Not for SMS or email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getosmo](https://clawhub.ai/user/getosmo)

### License/Terms of Use:

MIT-0

## Use Case:

People use this skill to make and manage real phone calls through OsmO, including contacting businesses, handling appointments and customer service, and reviewing calls to their OsmO number. It also guides users through account sign-in and call-screening settings.

### Deployment Geography for Use:

United States, Canada, United Kingdom, and Australia (free credits are available in these countries; some features require an OsmO app plan).

## Known Risks and Mitigations:

Risk: The security scan was partial, with 0% coverage because malformed manifest frontmatter prevented full inspection; the benign verdict has medium confidence.

Mitigation: Review the skill and OsmO service before enabling it, and confirm the service and sign-in pages are the expected OsmO destinations.

Risk: Calls reach real people and may involve requests or changes on the user's behalf.

Mitigation: Before placing a call, show the recipient and the exact message or request, then proceed only after the user agrees.

## Reference(s):

- [OsmO MCP server](https://api.getosmo.app/mcp)
- [OsmO](https://getosmo.app)

## Skill Output:

**Output Type(s):** [API Calls, Guidance, Text, Shell commands, Configuration instructions]

**Output Format:** [Phone call actions and status summaries, with Markdown guidance and inline shell or configuration examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calls and account changes require user approval; reports summarize results returned by OsmO.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
