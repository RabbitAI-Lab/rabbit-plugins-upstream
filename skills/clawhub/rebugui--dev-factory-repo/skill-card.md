## Description: <br>
Automates software development by discovering project ideas from GitHub trends, CVE data, and security news, then generating, testing, self-correcting, and publishing code through a multi-agent workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rebugui](https://clawhub.ai/user/rebugui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to discover candidate software projects, generate implementation work, run tests, apply limited self-correction, and publish completed projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local commands and generated tests. <br>
Mitigation: Install and run it only in an isolated workspace or VM with low-privilege credentials. <br>
Risk: Source or error snippets may be sent to external AI or cloud services. <br>
Mitigation: Review configuration and avoid processing sensitive source, secrets, or proprietary data unless the connected services are approved. <br>
Risk: GitHub and Notion integrations can update external systems with limited approval controls. <br>
Mitigation: Use least-privilege tokens, review Notion database access, and disable auto-publish until the exact commands and target repositories are approved. <br>
Risk: Scheduled jobs can repeatedly execute discovery, generation, testing, and publishing flows. <br>
Mitigation: Disable cron or scheduler entries until configuration, token scopes, and generated outputs have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rebugui/dev-factory-repo) <br>
- [Publisher profile](https://clawhub.ai/user/rebugui) <br>
- [Builder agent repository](https://github.com/rebugui/builder-agent) <br>
- [OpenClaw repository](https://github.com/rebugui/OpenClaw) <br>
- [ChatDev](https://github.com/OpenBMB/ChatDev) <br>
- [NVD CVE API](https://services.nvd.nist.gov/rest/json/cves/2.0) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or modify project files and publish generated repositories when configured with credentials.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
