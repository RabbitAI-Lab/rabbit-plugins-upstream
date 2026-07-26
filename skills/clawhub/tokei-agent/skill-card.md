## Description: <br>
Control Tokei (tokei.io) pre-launch and waitlist campaigns from the command line: list and update pages, clone new ones, pull stats and leaderboards, add entries, and manage webhooks via the Tokei v1 REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gilesdawe](https://clawhub.ai/user/gilesdawe) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, marketers, and launch operators use this skill to let agents inspect and manage Tokei waitlist and pre-launch campaigns through a CLI or MCP server. It supports monitoring, campaign updates, signup import, leaderboard review, and webhook management when the user supplies an appropriate Tokei API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent can read or modify Tokei campaign data when given a Tokei API key with sufficient scope. <br>
Mitigation: Use a read-only API key for monitoring and reserve read-write keys for tasks that are intended to change campaigns, entries, or webhooks. <br>
Risk: Changing TOKEI_API_URL could send requests and credentials to an untrusted endpoint. <br>
Mitigation: Leave TOKEI_API_URL unset for normal use, or set it only to an endpoint the user explicitly trusts. <br>
Risk: Webhook creation returns the signing secret only once. <br>
Mitigation: Store the returned webhook secret immediately and use HTTPS endpoints for webhook delivery. <br>
Risk: On Node 24 for Windows, the documented process exit code may be unreliable even when JSON output is correct. <br>
Mitigation: Judge command results by the JSON output envelope rather than the process exit status in that environment. <br>


## Reference(s): <br>
- [Tokei](https://tokei.io) <br>
- [Tokei API Reference](https://tokei.io/docs/api) <br>
- [Tokei OpenAPI Specification](https://tokei.io/openapi.json) <br>
- [ClawHub skill page](https://clawhub.ai/gilesdawe/skills/tokei-agent) <br>
- [Agent skill reference](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON API responses and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TOKEI_API_KEY; TOKEI_API_URL is optional and should only point to a trusted Tokei-compatible endpoint.] <br>

## Skill Version(s): <br>
0.2.2 (source: package.json, server.json, evidence.release.version, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
