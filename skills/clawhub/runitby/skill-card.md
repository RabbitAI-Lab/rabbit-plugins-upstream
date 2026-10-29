## Description:

Collect answers from people outside the chat by link. Make an open form, survey, poll or sign-up sheet anyone can fill (like a Tally or Google Form), ask specific people for details (a shipping address, client intake, availability, an RSVP), or get approval or sign-off from named people (human in the loop), then read the answers back as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aldrinsalazar](https://clawhub.ai/user/aldrinsalazar)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to collect structured answers from people outside a chat through open forms or person-specific requests, then read the responses as JSON. It can also request approvals from named people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Request details, recipient information, and answers pass through runitby.app, whose privacy and retention terms could not be independently verified.

Mitigation: Review the service's privacy and retention terms before sharing sensitive information.

Risk: Approval decisions may authorize consequential actions.

Mitigation: Keep recipients and approval actions within the intended scope, require email verification for consequential approvals, and act only on an approved verdict.

## Reference(s):

- [Run it by](https://runitby.app)
- [Run it by API reference](https://runitby.app/llms.txt)
- [Run it by OpenAPI specification](https://runitby.app/openapi.json)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [Shareable request links and validated JSON answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers follow the schema supplied with each request.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
