## Description: <br>
Automate Box cloud storage operations including file upload/download, search, folder management, sharing, collaborations, and metadata queries via Rube MCP (Composio). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to operate Box through Rube MCP for file transfers, content search, folder management, sharing and collaboration, metadata queries, and sign request handling. It is intended for workflows where the agent can confirm the Box connection and current tool schemas before acting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad access to Box file, folder, sharing, collaboration, and deletion actions through the configured MCP. <br>
Mitigation: Before acting, require confirmation of exact file or folder IDs, recipients, sharing settings, and any recursive or permanent deletion. <br>
Risk: Sharing changes or public links could expose Box content unintentionally. <br>
Mitigation: Avoid public links unless explicitly intended, and confirm recipients, roles, and download permissions before applying collaboration or sharing updates. <br>
Risk: Permanent removal or recursive deletion can cause irreversible data loss. <br>
Mitigation: Prefer trash or reversible actions where possible and reserve permanent removal for explicit user-approved requests. <br>


## Reference(s): <br>
- [Box Automation on ClawHub](https://clawhub.ai/sohamganatra/skills/box-automation) <br>
- [Rube MCP](https://rube.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with ordered MCP tool sequences and parameter notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Box workflow prerequisites, tool ordering, key parameters, pagination notes, permissions cautions, and common API pitfalls.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
