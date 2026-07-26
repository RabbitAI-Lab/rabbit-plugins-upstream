## Description: <br>
SmartRecruiters helps agents search and read SmartRecruiters jobs and candidates through the OOMOL-connected oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and recruiting operations teams use this skill to retrieve SmartRecruiters job and candidate information through OOMOL. It supports read-only workflows such as listing jobs, getting job details, searching candidates, and getting candidate details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Candidate records may contain sensitive recruiting data. <br>
Mitigation: Install and use this skill only in workspaces where SmartRecruiters access is appropriate, and avoid broad or ambiguous requests when candidate data should not be queried. <br>
Risk: The skill depends on OOMOL-managed CLI access and server-side credentials. <br>
Mitigation: Use the documented setup and recovery steps when authentication, connection, scope, credential, or billing errors occur. <br>


## Reference(s): <br>
- [SmartRecruiters skill page](https://clawhub.ai/oomol/skills/oo-smartrecruiters) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [SmartRecruiters homepage](https://www.smartrecruiters.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses from the connector include data and an executionId under meta.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
