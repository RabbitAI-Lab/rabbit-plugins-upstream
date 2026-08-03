## Description: <br>
Query and command a Kia vehicle directly with curl against the Kia Owners API, including vehicle status, location, EV charge state, locks, climate, and charging controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill for one-off shell-based reads and remote commands against their own Kia vehicle. It is intended for direct curl workflows when the Kia Access MCP server is not running or a quick status, location, lock, climate, or charging action is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose precise vehicle location and vehicle status through Kia account access. <br>
Mitigation: Require explicit user confirmation before retrieving location or other sensitive vehicle data, and run only in a trusted local environment. <br>
Risk: The skill can send remote vehicle commands such as unlocking doors, changing climate, or changing charging settings. <br>
Mitigation: Require explicit confirmation for every remote command and verify the intended vehicle and action before executing generated shell commands. <br>
Risk: Reusable Kia credentials and rmtoken values may be written to local session or header files. <br>
Mitigation: Treat the rmtoken like a password, use private files with restrictive permissions, avoid shared machines, and replace predictable temporary header paths with private temporary files. <br>


## Reference(s): <br>
- [Ready-to-run requests](references/requests.md) <br>
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess-curl) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON request bodies, and jq examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that read precise vehicle data or send remote vehicle actions when run with valid Kia credentials.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
