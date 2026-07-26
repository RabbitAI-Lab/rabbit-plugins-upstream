## Description: <br>
Look up salary for an Indeed job posting via RolesAPI.com using a job key or pasted Indeed URL, returning salary range, currency, period, and whether the value is employer-provided or estimated. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nikhonit](https://clawhub.ai/user/nikhonit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill when a user explicitly asks what a specific Indeed posting pays. It is suited for targeted salary lookups from an Indeed job key or viewjob URL, not market-wide salary estimates or full job-detail retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Each lookup sends the provided Indeed job key or URL to RolesAPI and may consume one API credit. <br>
Mitigation: Use the skill only for postings the user explicitly wants checked through RolesAPI, and make the credit-consuming lookup clear before running it. <br>
Risk: The skill depends on a ROLESAPI_KEY and an external RolesAPI request. <br>
Mitigation: Keep the API key in the environment, avoid exposing it in prompts or logs, and stop on authentication, credit, or network errors. <br>
Risk: Salary information can be absent from a posting, and the source may be employer-provided or estimated. <br>
Mitigation: Report the returned source field and clearly state when the API response omits salary data. <br>


## Reference(s): <br>
- [Indeed Salary on ClawHub](https://clawhub.ai/nikhonit/skills/indeed-salary) <br>
- [RolesAPI](https://rolesapi.com) <br>
- [RolesAPI API Keys](https://rolesapi.com/app/keys) <br>
- [RolesAPI Pricing](https://rolesapi.com/pricing/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Text] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ROLESAPI_KEY and performs one lookup for a provided Indeed job key or URL.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
