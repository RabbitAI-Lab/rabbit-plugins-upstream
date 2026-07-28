## Description: <br>
Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and your friend activity feed; and post check-ins, toasts, and comments to your own Untappd account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up Untappd beer, brewery, venue, profile, activity, and check-in data through the user's own account. It can also help log check-ins, toasts, and comments when the user explicitly confirms a write action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Untappd username and password credentials plus unofficial mobile app credentials, creating account, secret-handling, and platform-terms risk. <br>
Mitigation: Review before installing, use dedicated secret storage where possible, and install only when the user accepts the account and platform risks. <br>
Risk: Confirmed write tools can post check-ins, toasts, or comments publicly to the user's Untappd account. <br>
Mitigation: Require the dry-run preview to be reviewed and call write tools with confirm set to true only after explicit user approval. <br>
Risk: Check-in and beer-history data can be stored in a local SQLite cache or a remote per-user cache. <br>
Mitigation: Treat cached data as personal account data, limit access to the cache location, and disclose freshness or coverage caveats when answering history questions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Configuration] <br>
**Output Format:** [Markdown instructions and tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes dry-run previews for confirm-gated write actions and freshness or coverage caveats for cached check-in data.] <br>

## Skill Version(s): <br>
1.8.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
