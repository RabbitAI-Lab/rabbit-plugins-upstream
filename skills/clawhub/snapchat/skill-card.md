## Description:

Snapchat Marketing API integration with managed OAuth for managing ad accounts, campaigns, ad squads, ads, creatives, audiences, and performance stats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, advertisers, and developers use this skill to inspect and manage Snapchat advertising resources through Maton's authenticated gateway. It supports campaign operations, targeting, reporting, and connection management while requiring confirmation for write or authorization-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Maton API passthrough can reach any Snapchat endpoint authorized by the connected account, including endpoints outside the documented examples.

Mitigation: Use read and list calls first, grant the narrowest Snapchat scopes available, and confirm the target, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Maton API keys and provider-issued tokens can leak through logs, shell history, environment inspection, or shared terminal output.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, send raw API keys only to api.maton.ai, and rotate any key that was exposed.

Risk: Deleting a Snapchat connection is irreversible and can break automation that depends on the connection id.

Mitigation: List connections, match the exact connection id with the user, and run deletion only after explicit confirmation.

Risk: Snapchat API responses can contain account, organization, contact, or campaign data that should not be broadly exposed.

Mitigation: Extract only the fields needed for the task and avoid dumping full API responses into logs, files, or shared terminals.

Risk: Multiple Maton profiles or Snapchat connections can cause reads or writes to land in the wrong account.

Mitigation: Specify the intended Maton profile and Snapchat connection id whenever more than one account or connection is available.

## Reference(s):

- [Snapchat Ads API Introduction](https://developers.snap.com/api/marketing-api/Ads-API/introduction)
- [Snapchat API Patterns](https://developers.snap.com/api/marketing-api/Ads-API/api-patterns)
- [Snapchat Campaign Management](https://developers.snap.com/api/marketing-api/Ads-API/campaigns)
- [Snapchat Creative Management](https://developers.snap.com/api/marketing-api/Ads-API/creatives)
- [Snapchat Targeting](https://developers.snap.com/api/marketing-api/Ads-API/targeting)
- [Snapchat Ads Gallery API](https://developers.snap.com/api/marketing-api/Ads-Gallery-Api/using-the-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration guidance, Markdown guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Snapchat API paths, Maton CLI commands, request bodies, and response-field guidance.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
