## Description: <br>
Control Tokei pre-launch, waitlist, giveaway, referral, and launch campaigns from AI agents or the command line through the Tokei v1 REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gilesdawe](https://clawhub.ai/user/gilesdawe) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and marketing teams use this skill to let agents inspect, create, update, publish, and monitor Tokei campaign pages through a JSON-first CLI and local MCP server. It is suited to workflows that manage waitlists, giveaways, launch pages, media uploads, entries, surveys, stats, leaderboards, and webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A read+write Tokei API key allows the agent to create or modify public campaigns, upload selected media, add entries, publish or unpublish pages, and manage webhooks. <br>
Mitigation: Use a read-only API key for monitoring; provide a read+write key only for workflows that require changes, and review proposed write actions before execution. <br>
Risk: Webhook creation returns a signing secret only once. <br>
Mitigation: Capture and store the webhook secret securely at creation time, and rotate or recreate the webhook if the secret is lost. <br>
Risk: Campaign list fields such as prizes and reward tiers are replaced wholesale when updated. <br>
Mitigation: Read the current page state first, modify the complete list locally, and send the full intended list in the update. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gilesdawe/skills/tokei-agent) <br>
- [Tokei agent documentation](https://tokei.io/agent) <br>
- [Tokei API reference](https://tokei.io/docs/api) <br>
- [npm package](https://www.npmjs.com/package/tokei-agent) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TOKEI_API_KEY; write actions require a read+write key and should be reviewed before execution.] <br>

## Skill Version(s): <br>
0.3.0 (source: package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
