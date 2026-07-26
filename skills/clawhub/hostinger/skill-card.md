## Description: <br>
Manage Hostinger account via API - VPS administration, DNS zone management, domain portfolio, website hosting, Docker deployments, firewall, SSH key, and billing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rexlunae](https://clawhub.ai/user/rexlunae) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and site owners use this skill to administer Hostinger resources through agent-assisted command-line workflows. It supports VPS lifecycle operations, DNS and domain changes, Docker project management, firewall and SSH key management, hosting lookups, and billing account review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can administer live Hostinger resources, including servers, DNS records, domains, Docker deployments, firewalls, SSH keys, and billing data. <br>
Mitigation: Use the least-privileged Hostinger API token available, protect and rotate the token, and install only for agents that are expected to manage real Hostinger resources. <br>
Risk: Reset, restore, recreate, delete, nameserver, root-password, SSH-key, firewall, billing, and Docker deployment actions can disrupt production services or account state. <br>
Mitigation: Require explicit human approval before running these actions, and create backups or snapshots before high-impact server and DNS changes. <br>
Risk: Docker deployments can execute behavior defined by a compose file or URL that may come from outside the user's control. <br>
Mitigation: Review compose files and source URLs before deployment, and prefer trusted, pinned sources for deployment inputs. <br>


## Reference(s): <br>
- [Hostinger API Reference](references/api-endpoints.md) <br>
- [Hostinger Developer Documentation](https://developers.hostinger.com) <br>
- [Hostinger OpenAPI Specification](https://github.com/hostinger/api/blob/main/openapi.json) <br>
- [Hostinger Python SDK](https://github.com/hostinger/api-python-sdk) <br>
- [Hostinger CLI Tool](https://github.com/hostinger/api-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use a Hostinger API token stored in ~/.config/hostinger/token and return formatted JSON from API responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
