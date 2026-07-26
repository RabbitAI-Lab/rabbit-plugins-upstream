## Description: <br>
Creates or updates a proxied Cloudflare DNS A record when an agent needs to point a subdomain to an IPv4 address. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xieyuanqing](https://clawhub.ai/user/xieyuanqing) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to let an agent create or update Cloudflare DNS A records during deployment and DNS management workflows. It gathers a zone, record name, IP address, and optional proxy setting, then runs the included script and reports the Cloudflare API result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live Cloudflare DNS changes. <br>
Mitigation: Confirm the zone, record name, target IP address, and proxied setting before each run. <br>
Risk: A broadly scoped Cloudflare API token could allow unintended DNS edits. <br>
Mitigation: Use a Cloudflare API token limited to the specific zone and DNS-edit permission. <br>
Risk: Using a public-IP lookup may publish an address the user did not intend to expose. <br>
Mitigation: Avoid the public-IP lookup unless that is exactly the address intended for the DNS record. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xieyuanqing/skills/cloudflare-dns-updater) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, json, guidance] <br>
**Output Format:** [Markdown guidance with shell command execution details; successful runs include stdout status messages and a JSON DNS record object.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, requests, and a CLOUDFLARE_API_TOKEN environment variable with DNS edit permissions for the target zone.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
