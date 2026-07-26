## Description: <br>
Searches Indeed by keyword, location, and country and extracts structured job listing details including titles, companies, salaries, descriptions, benefits, and application links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and users use this skill to search Indeed job listings and collect structured job data for recruiting, market research, or job-search workflows. It operates through the user's browser session and is intended for data visible to that user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automates an active Indeed browser session and may use the user's logged-in state for pagination. <br>
Mitigation: Use it only for Indeed data visible in the intended browser session, verify login state before pagination, and avoid running it while unrelated sensitive pages are open. <br>
Risk: Batch shell and Python helper usage can make repeated browser requests and may trigger Indeed security checks or collect more data than intended. <br>
Mitigation: Review generated batch scripts before running them, test with one or two jobs first, keep batches small, and add delays between detail fetches. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/indeed-job-search) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, text] <br>
**Output Format:** [Markdown guidance with shell command templates and JSON data outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Structured job records may include HTML descriptions and nullable salary, benefits, rating, and apply-link fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
