## Description: <br>
Interact with Twenty CRM (self-hosted) via REST/GraphQL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jhumanj](https://clawhub.ai/user/jhumanj) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent query and manage records in a configured self-hosted Twenty CRM workspace through REST and GraphQL helpers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, modify, and delete CRM records in the configured Twenty workspace. <br>
Mitigation: Use a least-privilege API token and review every POST, PATCH, DELETE, or destroy command before execution. <br>
Risk: Credential and configuration handling is unclear and depends on a local environment file. <br>
Mitigation: Keep the environment file private, restrict filesystem access, and rotate the API token if exposure is suspected. <br>
Risk: Search and query input may be unsafe until URL encoding and config loading are hardened. <br>
Mitigation: Avoid untrusted search or query input and keep search terms simple until the helper scripts are hardened. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jhumanj/skills/twenty-crm) <br>
- [Publisher Profile](https://clawhub.ai/user/jhumanj) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON API payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May issue REST and GraphQL requests against the configured Twenty CRM workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
