## Description: <br>
Feishu Bitable API helps agents create, read, update, and delete Feishu Bitable tables, records, fields, and views through a Node.js CLI and API client. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stevenlikewatermelon](https://clawhub.ai/user/stevenlikewatermelon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation agents use this skill to integrate Feishu Bitable with workflows that manage tables, records, fields, and views. It is suited to task tracking, data synchronization, reporting, and other spreadsheet-like business data operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can directly change or delete live Feishu Bitable business data. <br>
Mitigation: Test on non-production tables first, back up important data, and manually verify app-token, table-id, and record-id values before running update or delete commands. <br>
Risk: The skill requires Feishu app credentials that can read and modify Bitable data. <br>
Mitigation: Use a least-privilege Feishu app and provide only the credentials needed for the intended tables and operations. <br>
Risk: JSON inputs can be loaded from @file paths and may affect table records in bulk. <br>
Mitigation: Review @file contents before execution and prefer small test batches before running broad create, update, or delete operations. <br>


## Reference(s): <br>
- [Feishu Open Platform](https://open.feishu.cn) <br>
- [Feishu Bitable API](https://open.feishu.cn/open-apis/bitable/v1) <br>
- [Feishu tenant access token API](https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/) <br>
- [ClawHub skill page](https://clawhub.ai/stevenlikewatermelon/skills/feishu-api-bitable) <br>
- [Publisher profile](https://clawhub.ai/user/stevenlikewatermelon) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with CLI shell commands and JSON request or response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Feishu app credentials and app, table, record, or file inputs depending on the command.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, package.json, publish-config.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
