## Description: <br>
Connects agents to the Cloudflare API for DNS management, tunnel management, and zone administration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucassynnott](https://clawhub.ai/user/lucassynnott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to inspect Cloudflare zones, manage DNS records, and create, configure, list, or delete Cloudflare tunnels from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real Cloudflare DNS and tunnel changes with the user's Cloudflare token. <br>
Mitigation: Use a least-privilege token limited to the needed account and zones, and review every DNS or tunnel change before running it. <br>
Risk: Stored Cloudflare API tokens and tunnel run tokens are secrets. <br>
Mitigation: Protect ~/.cloudflare_token with restrictive permissions, prefer scoped tokens, and treat tunnel run tokens printed to the terminal as confidential. <br>


## Reference(s): <br>
- [Cloudflare](https://cloudflare.com) <br>
- [Cloudflare API Tokens](https://dash.cloudflare.com/profile/api-tokens) <br>
- [Cloudflare API v4](https://api.cloudflare.com/client/v4) <br>
- [ClawHub Skill Page](https://clawhub.ai/lucassynnott/skills/cloudflare-api) <br>
- [Publisher Profile](https://clawhub.ai/user/lucassynnott) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, and tabular command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; Cloudflare API token access controls determine available account, zone, DNS, and tunnel operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
