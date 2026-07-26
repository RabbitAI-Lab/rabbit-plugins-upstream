## Description: <br>
Reusable Steam gaming companion for profiles, library insights, recommendations, wishlist tracking, achievement context, game lookups, reviews, setup verification, and preference memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[franciscoagx](https://clawhub.ai/user/franciscoagx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to help an agent work with Steam profiles, libraries, recommendations, wishlists, achievements, setup checks, game lookups, and review drafting. It depends on a configured steam-mcp server for live Steam data and can fall back to guidance from existing conversation context when live data is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain Steam profile preferences, notes, library, and wishlist context when persistent storage is configured. <br>
Mitigation: Use persistent storage only with appropriate user consent, avoid storing unnecessary sensitive notes, and clear stored profiles when they are no longer needed. <br>
Risk: Live Steam data depends on a separate steam-mcp integration and a configured Steam API key, and private or restricted Steam data may be unavailable. <br>
Mitigation: Verify setup and access status before relying on live data, and present private or missing data as unavailable instead of filling gaps with guesses. <br>
Risk: Recommendations, achievement summaries, and review help can be misleading when source data is stale, partial, or based only on stored preferences. <br>
Mitigation: Ground outputs in fetched snapshots and supplied candidate data, preserve privacy flags, and state uncertainty when the available data is incomplete. <br>


## Reference(s): <br>
- [steam-mcp repository](https://github.com/franciscoagx/steam-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration] <br>
**Output Format:** [Markdown responses supported by structured JSON context objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured steam-mcp server and Steam API key for live Steam data; may retain profile, library, wishlist, preference, and note context when persistent storage is configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and constants.ts) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
