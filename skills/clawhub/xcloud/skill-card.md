## Description: <br>
Official xCloud Public API plugin for agents: manage servers, sites, WordPress, SSL, account data, and API-driven hosting operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asif2bd](https://clawhub.ai/user/asif2bd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site operators, and hosting teams use this skill to let an agent inspect and operate xCloud hosting resources through the xCloud Public API. It supports server, site, WordPress, SSL, account, token, and deployment workflows when an authorized xCloud API token is configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent with a persistent xCloud API token can make real hosting and account changes. <br>
Mitigation: Use the narrowest scoped token available, prefer short-lived tokens, store tokens in the runtime secret store, and revoke exposed tokens promptly. <br>
Risk: Destructive or high-impact operations can affect production resources, including deletes, restores, reboots, token revocation, sudo or firewall changes, SSL provider changes, and deployments. <br>
Mitigation: Require explicit user confirmation before those actions and restate the target resource and operation before execution. <br>
Risk: Secrets and sensitive URLs may be exposed if users paste production tokens, private keys, passwords, or magic-login URLs into chat. <br>
Mitigation: Avoid pasting sensitive values into chat; use environment variables or secret stores and do not echo credentials or magic-login URLs back in responses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asif2bd/skills/xcloud) <br>
- [xCloud](https://xcloud.host) <br>
- [xCloud Dashboard](https://app.xcloud.host) <br>
- [User Guide](https://github.com/xCloudDev/xcloud-agent-skills/blob/main/docs/USER_GUIDE.md) <br>
- [Install Guide](https://github.com/xCloudDev/xcloud-agent-skills/blob/main/docs/SKILLS-GUIDE.md) <br>
- [Official GitHub](https://github.com/xCloudDev/xcloud-agent-skills) <br>
- [API Docs](https://app.xcloud.host/api/v1/docs) <br>
- [OpenClaw Tutorial](https://xcloud.host/openclaw-skills-and-clawhub-on-xcloud-openclaw-agent/) <br>
- [Tutorial Video](https://www.youtube.com/watch?v=oEE9OHo3_48) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and summarized xCloud API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, jq, and XCLOUD_API_TOKEN for authenticated operations.] <br>

## Skill Version(s): <br>
3.0.3 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
