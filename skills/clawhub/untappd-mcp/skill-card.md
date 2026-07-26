## Description: <br>
Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer Untappd questions about beers, breweries, venues, users, check-ins, wishlists, badges, friends, and venue menus. With explicit confirmation, it can also help post check-ins, toasts, and comments to the configured Untappd account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an Untappd username and password plus mobile-app client credentials obtained outside a normal OAuth flow. <br>
Mitigation: Install only after reviewing the underlying MCP server's credential storage and token transmission behavior, and keep secrets out of logs. <br>
Risk: Posting tools can affect the user's public Untappd account. <br>
Mitigation: Use the built-in dry-run preview behavior and require confirm: true before making posting calls. <br>
Risk: The local or remote cache may contain account activity data and incomplete history coverage. <br>
Mitigation: Treat cache contents as account activity data, protect the cache location, and rely on freshness and coverage caveats when interpreting not-found results. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/untappd-mcp) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance with tool names, configuration details, and account-action previews] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write actions are confirm-gated and cache-backed queries report freshness and coverage caveats.] <br>

## Skill Version(s): <br>
1.8.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
