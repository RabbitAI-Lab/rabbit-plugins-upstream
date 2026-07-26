## Description: <br>
Generates structured deep-research reports and imports them into Feishu Docs using a user-provided research topic and Feishu folder token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[henryjing96](https://clawhub.ai/user/henryjing96) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and research teams use this skill to collect multi-source research, generate a Markdown report with freshness and source coverage checks, and upload the result into a Feishu cloud folder. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Feishu app secrets, tenant access tokens, file tokens, tickets, or document tokens could be exposed in chat or logs. <br>
Mitigation: Configure credentials through a secure secret store and redact Feishu secrets and tokens from user-visible output and logs. <br>
Risk: Generated research may be uploaded to an unintended or sensitive Feishu folder. <br>
Mitigation: Use a least-privilege Feishu app, verify the target folder token before upload, and prefer non-sensitive folders for initial runs. <br>
Risk: A report may be misleading if source coverage or data freshness checks fail. <br>
Mitigation: Stop rather than downgrade when source count or date coverage is insufficient, and review the generated report before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/henryjing96/skills/feishu-deep-research) <br>
- [Feishu tenant access token API](https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal) <br>
- [Feishu file upload API](https://open.feishu.cn/open-apis/drive/v1/medias/upload_all) <br>
- [Feishu import tasks API](https://open.feishu.cn/open-apis/drive/v1/import_tasks) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report, Feishu document link, and structured execution summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses direct Feishu REST API calls and requires secure handling of Feishu app credentials, tenant access tokens, file tokens, tickets, and document tokens.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
