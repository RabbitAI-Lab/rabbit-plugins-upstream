## Description: <br>
Search Indeed job postings by keyword and location via RolesAPI.com, returning job listings as JSON with filters for postings from today, this week, or remote-only across 60+ country editions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nikhonit](https://clawhub.ai/user/nikhonit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers, recruiters, and agents assisting users use this skill to search Indeed job postings by keyword and location, including recent postings and remote-only listings through RolesAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends job-search keywords and locations to RolesAPI using a RolesAPI key. <br>
Mitigation: Install and use it only when sharing those search terms with RolesAPI is acceptable, and store ROLESAPI_KEY only in trusted agent environments. <br>
Risk: Searches consume RolesAPI credits, especially when multi-page options are used. <br>
Mitigation: Use focused searches and cap max-pages for exploratory scans. <br>


## Reference(s): <br>
- [Indeed Search on ClawHub](https://clawhub.ai/nikhonit/skills/indeed-search) <br>
- [RolesAPI](https://rolesapi.com) <br>
- [RolesAPI pricing](https://rolesapi.com/pricing/) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON response envelopes with Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ROLESAPI_KEY. Searches send job-search keywords and locations to RolesAPI and consume RolesAPI credits, especially when multi-page options are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
