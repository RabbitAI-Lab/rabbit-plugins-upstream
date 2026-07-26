## Description: <br>
Search for jobs across LinkedIn, Indeed, Glassdoor, ZipRecruiter, Google Jobs, Bayt, Naukri, and BDJobs using the JobSpy MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amoghpurohit](https://clawhub.ai/user/amoghpurohit) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to search and compare job listings across multiple job boards with filters for role, location, platform, recency, salary, job type, remote work, and easy-apply options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches may send job terms, locations, and filters to the configured JobSpy MCP server and external job boards. <br>
Mitigation: Avoid sensitive personal details in search queries and review the referenced MCP server and packages before use. <br>
Risk: Large or LinkedIn-heavy searches can trigger rate limits, timeouts, or incomplete results. <br>
Mitigation: Start with small result counts, prefer reliable sites such as Indeed, and split or narrow searches when errors occur. <br>
Risk: The skill requires running third-party Python or Node.js MCP server components locally. <br>
Mitigation: Use a virtual environment, review dependencies, and keep packages updated before connecting the server to an agent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/amoghpurohit/skills/job-search-mcp) <br>
- [JobSpy MCP server repository](https://github.com/chinpeerapat/jobspy-mcp-server.git) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON MCP tool calls and shell or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces filtered job-search requests and job-listing response shapes with fields such as title, company, location, salary, posting date, job URL, and remote status.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
