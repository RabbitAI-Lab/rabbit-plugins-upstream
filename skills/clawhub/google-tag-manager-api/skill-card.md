## Description: <br>
Google Tag Manager API integration with managed OAuth for managing GTM accounts, containers, workspaces, tags, triggers, variables, environments, container versions, and user permissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect and administer Google Tag Manager resources through Maton-managed OAuth. It supports listing and managing accounts, containers, workspaces, tags, triggers, variables, environments, versions, publishing actions, and user permissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Maton proxies Google Tag Manager API requests and handles the OAuth connection. <br>
Mitigation: Install only if you trust Maton with the connected GTM account and protect MATON_API_KEY as a credential. <br>
Risk: Write, delete, permission, and publish operations can change GTM resources or make container changes live. <br>
Mitigation: Before approving writes, confirm the exact account, container, workspace, resource, permission target, and whether publishing will make changes live. <br>
Risk: Multiple Maton GTM connections could route requests to an unintended account. <br>
Mitigation: Use the Maton-Connection header when more than one GTM connection exists. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-tag-manager-api) <br>
- [Maton Homepage](https://maton.ai) <br>
- [Google Tag Manager API Overview](https://developers.google.com/tag-platform/tag-manager/api/v2) <br>
- [Google Tag Manager API Reference](https://developers.google.com/tag-platform/tag-manager/api/reference/rest) <br>
- [Google Tag Manager Concepts](https://developers.google.com/tag-platform/tag-manager/api/v2/devguide) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls] <br>
**Output Format:** [Markdown with inline HTTP paths and Python, JavaScript, or shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, Maton OAuth connection, and user approval before write or publish operations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
