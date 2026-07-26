## Description: <br>
Manages and troubleshoots Volcengine cloud phone resources through a local Python CLI and OpenAPI client, including instances, resources, screenshots, commands, tasks, apps, hosts, capacity, tags, DNS, routes, and authorized test cloud phone operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volcengine-skills](https://clawhub.ai/user/volcengine-skills) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to inspect, administer, and troubleshoot authorized Volcengine cloud phone test resources from an agent-assisted CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact cloud phone administration actions, including create, delete, billing/resource, network, file, and command operations. <br>
Mitigation: Use least-privilege test credentials and require explicit user confirmation before any state-changing action. <br>
Risk: Credential files, access keys, authorization headers, and signed URLs can expose access to cloud phone resources. <br>
Mitigation: Keep config.json and signed URLs private, and do not display secrets or complete signed URLs unless the user explicitly requests them. <br>
Risk: The generic action-call command can invoke raw OpenAPI actions outside the more specific documented command paths. <br>
Mitigation: Use action-call only after reviewing the exact OpenAPI action and parameters. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands and concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that call Volcengine OpenAPI endpoints and may summarize JSON API responses.] <br>

## Skill Version(s): <br>
1.2.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
