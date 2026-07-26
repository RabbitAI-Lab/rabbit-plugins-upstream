## Description: <br>
密码生成器Pro免费版为个人用户提供强密码生成、密码强度检测、口令短语生成和 PIN 码生成能力。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to create personal account passwords, generate memorable passphrases or PINs, and receive basic password strength feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated passwords or tested passwords may appear in terminal output, agent transcripts, or logs. <br>
Mitigation: Avoid testing real account passwords, review log handling before use, and clear sensitive output from shared workspaces. <br>
Risk: Password audit examples may encourage plaintext password lists. <br>
Mitigation: Use sample data where possible and avoid storing real password lists in plaintext files. <br>
Risk: The artifact documents an optional callback URL field without evidence that secrets are never sent externally. <br>
Mitigation: Do not provide callback URLs for secret-bearing tasks unless the publisher documents the data flow and handling guarantees. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/password-gen-pro-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with code blocks and optional JSON-like result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include generated passwords, generated PINs, generated passphrases, and password strength summaries.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
