## Description: <br>
Bilibili Toolkit helps agents guide Bilibili video publishing, high-resolution downloads, batch operations, analytics tracking, and credential handling for creator and operations workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, operations teams, and developers use this skill to guide Bilibili account automation tasks such as video upload, scheduled publishing, batch downloading, metrics tracking, comparison analysis, and credential handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide account actions that publish, edit, schedule, or download Bilibili content through an agent with exec capability. <br>
Mitigation: Review commands and parameters before execution, use the least capable account suitable for the task, and confirm account-impacting actions before running them. <br>
Risk: The skill uses Bilibili session cookies, including SESSDATA and bili_jct, that can act like account passwords. <br>
Mitigation: Provide credentials only in trusted environments, avoid persistence unless necessary, protect persisted files, and clear credentials after use. <br>
Risk: The artifact includes inconsistent LLM and security-review instructions that may confuse what data is required or where it is sent. <br>
Mitigation: Do not provide unrelated LLM or API keys unless the publisher clarifies why they are needed and what data will be transmitted. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/bilibili-toolkit) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Python and shell command examples plus JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may involve Bilibili session cookies, local command execution, optional credential persistence, and account actions such as publishing or editing content.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
