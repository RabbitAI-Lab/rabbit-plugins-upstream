## Description: <br>
Job Auto Apply guides an agent through job-search and application automation, including profile setup, dry runs, batch application commands, retries, and execution logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External job seekers and agent users use this skill to prepare a job profile, search roles, run dry-run application flows, and optionally submit applications with confirmation and logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use broad execution capability during job-application automation. <br>
Mitigation: Run it in a constrained workspace and avoid granting command execution or file access outside job-search materials. <br>
Risk: The skill may process personal profile data while preparing or submitting applications. <br>
Mitigation: Use a dedicated job profile containing only information you are comfortable sharing with target employers and job platforms. <br>
Risk: The skill can move from dry-run planning to real application submission. <br>
Mitigation: Keep dry-run enabled until each application is inspected, and require explicit confirmation before any submission. <br>


## Reference(s): <br>
- [Job Auto Apply ClawHub Skill Page](https://clawhub.ai/thcjp/skills/job-auto-apply) <br>
- [thcjp Publisher Profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON result structures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local profile files, dry-run mode, confirmation gates, retries, and execution logs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
