## Description: <br>
Job Auto Apply Tool Free helps individual job seekers search LinkedIn and Indeed, match roles to a profile, generate tailored cover letters, and submit applications with dry-run and confirmation controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and individual job seekers use this skill to automate job search and application preparation across supported hiring platforms while retaining dry-run and manual confirmation controls. It is suited for personal job search workflows, not high-volume recruiting operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read sensitive job profile and resume data. <br>
Mitigation: Provide only the personal data needed for the target applications and avoid storing extra profile details until data handling is documented clearly. <br>
Risk: The skill may use recruitment platform credentials or API keys. <br>
Mitigation: Use dedicated credentials where possible, limit account permissions, and remove credentials when the workflow is complete. <br>
Risk: The skill can submit real job applications. <br>
Mitigation: Run in dry-run mode first, require explicit confirmation for every submission, and keep daily application limits low. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/job-auto-apply-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON configuration/output snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate job profile configuration, cover-letter text, execution logs, and application status summaries.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
