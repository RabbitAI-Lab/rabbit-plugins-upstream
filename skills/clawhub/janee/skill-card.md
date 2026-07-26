## Description: <br>
Secrets management for AI agents. Never expose your API keys again. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rsdouglas](https://clawhub.ai/user/rsdouglas) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Janee to let MCP-capable agents call configured APIs without directly exposing stored API keys. The skill focuses on local encrypted key storage, request policies, audit logs, and OpenClaw integration for controlled API access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may receive broad authenticated API access if capabilities are configured too broadly. <br>
Mitigation: Use narrowly scoped API keys and define explicit allow and deny rules for every capability before enabling agent access. <br>
Risk: Automatic approval, sessions, and revocation are not strong safety controls for sensitive operations. <br>
Mitigation: Avoid production financial or write-capable credentials and require human review for sensitive or irreversible API actions. <br>
Risk: Local Janee configuration, backups, session records, and logs may expose sensitive operational details. <br>
Mitigation: Treat `~/.janee/config.yaml`, backups, sessions, and logs as sensitive local files with restrictive filesystem access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rsdouglas/skills/janee) <br>
- [GitHub repository](https://github.com/rsdouglas/janee) <br>
- [npm package](https://www.npmjs.com/package/@true-and-useful/janee) <br>
- [OpenClaw plugin package](https://www.npmjs.com/package/@true-and-useful/janee-openclaw) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>
- [Path-Based Request Policies](docs/POLICIES.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown with inline shell commands, YAML examples, and tool call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local configuration and MCP/OpenClaw usage guidance; API responses depend on the configured external service.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata; artifact frontmatter is 0.1.0 and package.json is 0.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
