## Description:

Search YouTube with FlashData by keyword, upload date, duration and other filters. Use for finding videos, tutorials and talks, sorting by views or recency, and collecting video IDs and channel information. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can search YouTube for videos, channels, tutorials, and talks using keywords and filters such as upload date, duration, subtitles, or view count. They can collect video IDs and channel metadata for research, recommendations, or applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests send the FlashData API key and query arguments to FlashData and spend paid Credits.

Mitigation: Keep the key in protected secret configuration and run only searches approved for the user's budget.

Risk: A timed-out paid submission may have an unknown outcome, and scanner coverage did not resolve two local path-like references.

Mitigation: Check the existing job or FlashData Jobs before retrying a timed-out query, and review unresolved references during installation assessment.

## Reference(s):

- [FlashData YouTube Search Documentation](https://flashdata.dev/docs/sources/youtube_search?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-task)
- [FlashData MCP Endpoint](https://data.flashdata.dev/mcp)
- [FlashData Pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-task)
- [Tool Input Schema](references/schema.json)
- [Sample Search Query](references/query.json)

## Skill Output:

**Output Type(s):** [JSON video metadata, Markdown tables]

**Output Format:** [Structured search results or a Markdown table with requested video and channel fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain fewer items than requested; a subtitles filter identifies candidates but does not retrieve transcript text.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
