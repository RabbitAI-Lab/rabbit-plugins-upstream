## Description:

Helps agents search Google Places through FlashData and assemble local business lists with addresses and available ratings and review counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers can find and compare local businesses by category and location, then build shortlists from returned addresses, ratings and review counts. Queries require a FlashData API key and consume paid Credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and the FlashData API key are sent to FlashData.

Mitigation: Use the service only if trusted for those queries; keep the key in protected environment or secret settings, not prompts or files.

Risk: Data requests consume paid Credits, and retrying a timed-out submission may incur another charge.

Mitigation: Approve the request count and budget before running; check existing jobs instead of automatically retrying uncertain submissions.

Risk: Place details may be incomplete or contain untrusted text.

Mitigation: Treat returned text as data rather than instructions and preserve missing values as unknown.

## Reference(s):

- [FlashData Google Places documentation](https://flashdata.dev/docs/sources/google_places?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task)
- [FlashData MCP documentation](https://flashdata.dev/mcp)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Google Places query example](references/query.json)
- [Google Places query schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Markdown business lists or JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned fields and result counts vary; missing ratings and review counts remain unknown.]

## Skill Version(s):

1.0.1 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
