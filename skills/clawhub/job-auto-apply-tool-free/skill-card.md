## Description: <br>
A lightweight job application automation skill for searching LinkedIn and Indeed roles, matching them against a user profile, and drafting tailored cover letters with dry-run and confirmation options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual job seekers, new graduates, and career changers use this skill to search job platforms, compare roles with their profile, generate cover-letter text, and prepare controlled application submissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may expose resume, profile, contact, salary, authorization, or job-preference data to job platforms or any LLM used to generate cover letters. <br>
Mitigation: Use dry-run mode first, review the profile data before use, and only provide information that is appropriate to send to the selected platforms and model. <br>
Risk: The skill may require access to LinkedIn, Indeed, or other job-platform credentials and tokens. <br>
Mitigation: Keep credentials out of prompts and tracked files, prefer environment variables or a secret manager, and rotate tokens if they are exposed. <br>
Risk: Optional confirmation controls could allow unintended or low-quality applications if disabled. <br>
Mitigation: Require manual confirmation for every submission and verify each role, generated cover letter, and application payload before sending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/job-auto-apply-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local profile files, resume paths, platform credentials, dry-run settings, and per-application confirmation controls.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
