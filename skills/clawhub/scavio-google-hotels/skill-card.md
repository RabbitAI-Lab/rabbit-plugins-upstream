## Description: <br>
Search Google Hotels for a destination and dates, then fetch per-property vendor pricing and full details as structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travel-focused agents, developers, and operators use this skill to search lodging for specific destinations and stay dates, compare price/rating/class/amenity filters, and retrieve vendor pricing for selected properties. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel search details, stay dates, and selected property identifiers are sent to Scavio. <br>
Mitigation: Install only when that data sharing is acceptable and use a user-provided SCAVIO_API_KEY. <br>
Risk: Each documented API call consumes one Scavio credit. <br>
Mitigation: Run search and detail calls deliberately, page results only when needed, and monitor credits_remaining. <br>
Risk: Hotel prices and vendor availability may change before booking. <br>
Mitigation: State the requested currency and stay dates, and verify prices with the booking vendor before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-hotels) <br>
- [Scavio Google Hotels documentation](https://scavio.dev/docs/google-hotels) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, Python examples, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses include hotel properties, detail tokens, booking sources, credit usage, and cache status.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
