## Description: <br>
Pull LinkedIn person and company profiles, posts, contact info, company people and jobs, and search people, jobs, and posts as structured JSON. 14 endpoints for prospecting, recruiting, and market research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to retrieve LinkedIn profile, company, job, post, and search data through Scavio for prospecting, recruiting, and market research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Retrieved LinkedIn contact and profile data may be privacy-sensitive. <br>
Mitigation: Use the skill only for lawful and permitted workflows; avoid bulk enrichment or unsolicited outreach unless allowed by relevant platform terms and applicable law. <br>
Risk: Paginated searches can consume Scavio API credits quickly. <br>
Mitigation: Warn before deep pagination and monitor credits_remaining in API responses. <br>
Risk: LinkedIn upstream responses can be slow or temporarily unavailable. <br>
Mitigation: Use a client timeout of at least 60 seconds and retry transient 502 or 503 failures after a short delay. <br>


## Reference(s): <br>
- [Scavio LinkedIn API documentation](https://scavio.dev/docs/linkedin-api) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-linkedin) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with code examples and structured JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls consume Scavio credits and may paginate.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
