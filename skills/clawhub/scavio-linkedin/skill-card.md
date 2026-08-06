## Description: <br>
Pull LinkedIn person and company profiles, their posts, job listings and post comments as structured JSON. 9 endpoints from 1 to 30 credits, four of them paginated, for prospecting, recruiting, and market research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve structured public LinkedIn profile, company, job, post, and comment data for prospecting, recruiting, and market research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkedIn handles, URLs, job IDs, post IDs, and related queries are sent to Scavio. <br>
Mitigation: Use the skill only for legitimate, user-directed research and avoid bulk profiling or monitoring individuals. <br>
Risk: Public LinkedIn activity can be privacy-sensitive or easy to overinterpret. <br>
Mitigation: Return only API data and avoid inferring private details from public activity. <br>
Risk: Paginated endpoints and full job lookups can consume credits quickly. <br>
Mitigation: Cap page counts, disclose intended credit use before paging, and call the 30-credit job detail endpoint only for listings the user selected. <br>
Risk: Retired endpoints return permanent 410 responses. <br>
Mitigation: Treat 410 responses as unavailable data, do not retry them, and do not substitute guessed values. <br>


## Reference(s): <br>
- [Scavio LinkedIn API documentation](https://scavio.dev/docs/linkedin-api) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub scavio-linkedin release page](https://clawhub.ai/scavio-ai/skills/scavio-linkedin) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance, Shell commands, Code] <br>
**Output Format:** [Structured JSON responses with concise Markdown guidance and optional shell or Python examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; output may include public LinkedIn profile, company, job, post, and comment data returned by Scavio.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
