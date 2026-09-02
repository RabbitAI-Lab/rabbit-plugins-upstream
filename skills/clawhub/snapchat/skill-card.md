## Description:

Snapchat Marketing API integration with managed OAuth for managing ad accounts, campaigns, ad squads, ads, creatives, audiences, targeting, and performance stats through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External advertisers, marketing operators, and developers use this skill to inspect and manage Snapchat Marketing API resources, including campaigns, creatives, audiences, targeting, and stats through approved Maton-authenticated calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton acts as the gateway and CLI provider for Snapchat ad-account access.

Mitigation: Confirm trust in Maton before installation and prefer OAuth so credentials stay in the operating system credential store.

Risk: Write operations can create, update, delete, publish, or otherwise affect Snapchat advertising resources.

Mitigation: Default to read and list calls, then require explicit user approval with target resource, payload, and intended effect before POST, PUT, PATCH, DELETE, or connection creation.

Risk: Multiple Maton profiles or Snapchat connections can route requests to the wrong account.

Mitigation: Specify the intended connection and profile when more than one exists.

Risk: Later examples omit the `/snapchat/...` path prefix, which can cause failed or ambiguous CLI calls.

Mitigation: Prefer `/snapchat/...` paths for `maton api` calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/snapchat)
- [Maton](https://maton.ai)
- [Snapchat Ads API Introduction](https://developers.snap.com/api/marketing-api/Ads-API/introduction)
- [Snapchat API Patterns](https://developers.snap.com/api/marketing-api/Ads-API/api-patterns)
- [Snapchat Campaign Management](https://developers.snap.com/api/marketing-api/Ads-API/campaigns)
- [Snapchat Creative Management](https://developers.snap.com/api/marketing-api/Ads-API/creatives)
- [Snapchat Targeting](https://developers.snap.com/api/marketing-api/Ads-API/targeting)
- [Snapchat Ads Gallery API](https://developers.snap.com/api/marketing-api/Ads-Gallery-Api/using-the-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit approval for connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence; artifact frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
