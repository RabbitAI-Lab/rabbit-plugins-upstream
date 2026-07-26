## Description: <br>
SaleSmartly API Skills helps agents use provided scripts for customer, session, marketing, WhatsApp, and reporting workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binzaga](https://clawhub.ai/user/binzaga) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers who operate SaleSmartly can ask an agent to query customer and conversation data, generate sales or feedback reports, manage WhatsApp devices, and run approved customer-management scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release bundles an api-key.json file and can expose sensitive SaleSmartly credentials if installed unchanged. <br>
Mitigation: Remove the bundled api-key.json before installation, create a local configuration from the example file, and prefer environment variables or a private config path for credentials. <br>
Risk: The skill can access customer data, chat history, webhook exports, and broad reporting data through local scripts. <br>
Mitigation: Review requested commands before execution, restrict credentials to the minimum required SaleSmartly project permissions, and require explicit approval before exporting chat history or sending DingTalk/webhook reports. <br>
Risk: Some scripts perform mutations or bulk actions such as creating or updating customers, assigning sessions, changing tags, sending messages, or deleting WhatsApp devices. <br>
Mitigation: Require explicit user confirmation for destructive, bulk, or message-sending operations and review generated or selected commands before running them. <br>
Risk: The artifact includes local agent settings that may change approval behavior. <br>
Mitigation: Review or delete .claude/settings.local.json before use and confirm that the agent requires approval for destructive operations, bulk changes, chat-history access, and webhook export. <br>


## Reference(s): <br>
- [SaleSmartly API documentation](https://salesmartly-api.apifox.cn/llms.txt) <br>
- [SaleSmartly API header signing guide](https://help.salesmartly.com/docs/API-Header) <br>
- [Authentication reference](references/authentication.md) <br>
- [No direct API usage guide](NO-DIRECT-API.md) <br>
- [Scripts reference](scripts/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [All documented scripts support structured --json output for agent parsing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
