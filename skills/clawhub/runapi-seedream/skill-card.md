## Description: <br>
Generate and edit images with Seedream through RunAPI for one-off CLI tasks or application integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate or edit Seedream images through RunAPI. It guides agents toward the RunAPI CLI for one-off generation and SDKs for app or backend integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may spend RunAPI account quota or incur costs when generating or editing images. <br>
Mitigation: Install and enable the skill only in environments intended to use RunAPI for Seedream, and review account costs before use. <br>
Risk: RUNAPI_API_KEY or saved CLI login could expose RunAPI access to agents that should not have it. <br>
Mitigation: Provide RunAPI credentials only in trusted environments where the agent is authorized to use that account. <br>
Risk: Generated RunAPI file URLs are temporary and may not be suitable as durable assets. <br>
Mitigation: Download and store generated outputs in durable storage within the retention window described by the skill. <br>


## Reference(s): <br>
- [RunAPI Seedream Model Overview](https://runapi.ai/models/seedream) <br>
- [RunAPI Seedream Documentation](https://runapi.ai/models/seedream.md) <br>
- [RunAPI Model Catalog](https://runapi.ai/models.md) <br>
- [ByteDance Provider Page](https://runapi.ai/providers/bytedance.md) <br>
- [RunAPI CLI Skill](https://github.com/runapi-ai/cli-skill) <br>
- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-seedream) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include RunAPI CLI commands, SDK package names, request JSON, and credential setup guidance.] <br>

## Skill Version(s): <br>
0.2.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
