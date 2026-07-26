## Description: <br>
Answers n8n questions and builds n8n workflows, node configurations, Code node JavaScript, HTTP Request setups, API integrations, toolbox-assisted API tests, and importable workflow JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[billzhuang6569](https://clawhub.ai/user/billzhuang6569) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation builders use this skill to answer n8n questions, design workflows, configure nodes, draft Code node JavaScript, build HTTP Request integrations, and produce importable workflow JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated n8n workflows, HTTP calls, or helper scripts may perform external changes when executed with real credentials. <br>
Mitigation: Use dry-run modes first, review workflows before import or activation, and only run execution modes or real API calls when the change is intended. <br>
Risk: Workflow JSON, examples, or logs could expose API keys, OAuth tokens, cookies, app secrets, or other sensitive credentials if copied directly from a real environment. <br>
Mitigation: Keep secrets in environment variables or n8n credentials, use placeholders in generated artifacts, and avoid printing or storing real credentials. <br>
Risk: Generated automations may include incorrect node settings, API fields, permissions, or response paths. <br>
Mitigation: Prefer the bundled references and official documentation, validate importable workflow JSON, and review node configuration before activation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/billzhuang6569/n8n-master) <br>
- [SKILL.md](SKILL.md) <br>
- [Workflow JSON validator](scripts/validate_workflow_json.py) <br>
- [n8n documentation](https://docs.n8n.io/) <br>
- [n8n HTTP Request node documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, JavaScript, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated n8n workflow JSON should remain inactive until reviewed and credentials are bound after import.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
