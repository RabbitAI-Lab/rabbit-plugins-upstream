## Description: <br>
Freshteam lets agents search and read Freshteam HR and recruiting data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and developers use this skill to retrieve Freshteam employees, job postings, applicant fields, job posting fields, candidate sources, and related directory data without handling raw credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Freshteam HR and recruiting data through the user's connected account. <br>
Mitigation: Install only for users who should access that Freshteam data, and verify the OOMOL CLI and Freshteam connection are controlled by the user or organization. <br>
Risk: Future Freshteam actions that write, delete, or change data could affect production HR or recruiting records. <br>
Mitigation: Require explicit user approval for any action marked as write, destructive, or state-changing before running it. <br>


## Reference(s): <br>
- [Freshteam Skill Page](https://clawhub.ai/oomol/skills/oo-freshteam) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Freshteam Homepage](https://www.freshworks.com/freshteam/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include JSON data and a metadata execution ID when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
