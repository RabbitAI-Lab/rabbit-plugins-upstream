## Description: <br>
Queries Huawei Cloud CES/EPS monitoring and enterprise project resources, including alarm rules, histories, templates, dashboards, notification masks, resource groups, one-click alarms, enterprise projects, quotas, bound resources, and migration records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operations engineers, and support teams use this skill to inspect Huawei Cloud monitoring and enterprise project state without creating, modifying, or deleting resources. It helps agents gather alarm, dashboard, resource group, quota, bound-resource, and migration information from actual Huawei Cloud API responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup path can create a virtual environment and install Python dependencies on the local host. <br>
Mitigation: Review setup behavior before installation and run the skill in an isolated, disposable environment when possible. <br>
Risk: TLS certificate verification is disabled in the HTTP configuration while the skill handles Huawei Cloud credentials. <br>
Mitigation: Fix or restore TLS verification before use on sensitive hosts, and avoid untrusted networks until that change is verified. <br>
Risk: The skill requires Huawei Cloud access keys and may validate credentials by calling Huawei Cloud APIs. <br>
Mitigation: Use least-privilege, scoped credentials and avoid exposing environment variable values in prompts, logs, or output. <br>
Risk: Dependencies are declared with lower-bound version ranges and may be installed dynamically. <br>
Mitigation: Prefer pinned dependencies or a prebuilt trusted environment for production use. <br>


## Reference(s): <br>
- [CES Python Script Usage Guide](references/ces/guide.md) <br>
- [Enterprise Project EPS Python Script Usage Guide](references/eps/guide.md) <br>
- [ClawHub Skill Listing](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-monitoring-query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell command snippets and summarized JSON or text query results from Huawei Cloud scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only query workflows; returned fields and result sizes depend on Huawei Cloud API responses, configured credentials, region, project scope, and script parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
