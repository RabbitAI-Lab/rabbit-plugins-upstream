## Description: <br>
Manage Nginx Proxy Manager (NPM) hosts, certificates, and access lists for adding domains, routing domains to services, enabling SSL, and checking proxy host status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weird-aftertaste](https://clawhub.ai/user/weird-aftertaste) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to inspect and manage Nginx Proxy Manager proxy hosts, certificates, and access lists through documented commands and REST API workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live Nginx Proxy Manager changes, including deleting proxy hosts. <br>
Mitigation: Review every generated API request before execution and avoid delete operations on production hosts without an independent backup and rollback plan. <br>
Risk: The helper caches an admin token at /root/.npm-token.json with weak guardrails. <br>
Mitigation: Install only in a trusted environment, protect NPM admin credentials and the cached token file, and remove or rotate the token when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/weird-aftertaste/skills/npm-proxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, Python script usage, and JSON API payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide live Nginx Proxy Manager API operations, including enabling, disabling, or deleting proxy hosts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
