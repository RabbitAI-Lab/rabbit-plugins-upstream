## Description: <br>
Search Untappd beers, breweries, venues, user activity, and account data, and post check-ins, toasts, or comments to the configured Untappd account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Untappd beer, brewery, venue, and user information through an agent, and to perform confirmed public account actions such as check-ins, toasts, and comments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires raw Untappd account credentials and private mobile API credentials. <br>
Mitigation: Install only after confirming the user accepts this credential exposure, and use dedicated or rotated credentials where feasible. <br>
Risk: The skill can post check-ins, toasts, and comments as public Untappd account actions. <br>
Mitigation: Require explicit user confirmation before posting and treat previews as the review point for account-visible changes. <br>
Risk: The skill stores check-in history in a local or remote cache. <br>
Mitigation: Limit cache access to authorized users, review cache storage location, and clear cached data when it is no longer needed. <br>
Risk: The skill can inspect other users' Untappd activity where visibility allows. <br>
Mitigation: Use it only for legitimate purposes with appropriate visibility, consent, or relationship context. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance describing Untappd queries, account actions, cache status, and setup values.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe dry-run previews, pagination state, cache freshness, and completion caveats when applicable.] <br>

## Skill Version(s): <br>
1.8.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
