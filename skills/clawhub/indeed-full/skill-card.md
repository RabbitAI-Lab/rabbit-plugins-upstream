## Description: <br>
Complete Indeed job postings toolkit via RolesAPI.com. Search Indeed job postings by keyword and location, fetch full role details, look up salary for a job posting, and get descriptions, company info, and benefits across 60+ country editions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nikhonit](https://clawhub.ai/user/nikhonit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, recruiters, and job-market analysts use this skill to search Indeed postings and retrieve normalized job, salary, company, description, and benefits data through RolesAPI when a user explicitly requests job data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Job searches, locations, job keys, and pasted Indeed URLs are sent to RolesAPI. <br>
Mitigation: Use the skill only for explicit job-data requests and avoid submitting sensitive or unnecessary personal context in search terms or URLs. <br>
Risk: Account checks can expose RolesAPI plan, rate limit, credit balance, and recent usage in the agent output. <br>
Mitigation: Run account and usage checks only when needed, and avoid sharing their output in contexts where billing or usage details should remain private. <br>
Risk: Most data lookups consume RolesAPI credits. <br>
Mitigation: Confirm ambiguous user intent before running scripts and prefer narrower endpoints such as salary, company, benefits, or description when a full posting is unnecessary. <br>


## Reference(s): <br>
- [RolesAPI](https://rolesapi.com) <br>
- [RolesAPI OpenAPI Specification](https://rolesapi.com/openapi.json) <br>
- [RolesAPI Roles API Documentation](https://rolesapi.com/api/roles/) <br>
- [RolesAPI Listings API Documentation](https://rolesapi.com/api/listings/) <br>
- [ClawHub Skill Page](https://clawhub.ai/nikhonit/skills/indeed-full) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and pretty-printed JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ROLESAPI_KEY; job searches, locations, job keys, pasted Indeed URLs, and account checks are sent to RolesAPI.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
