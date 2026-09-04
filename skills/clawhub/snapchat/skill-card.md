## Description:

Snapchat Marketing API integration with managed OAuth for managing ad accounts, campaigns, ad squads, ads, creatives, audiences, performance stats, and targeting through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing operators use this skill to inspect and manage Snapchat advertising resources, including campaigns, ad squads, ads, creatives, audiences, targeting, and stats. The skill is intended for Maton-mediated Snapchat API workflows where read/list calls are the default and write actions require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on Snapchat advertising accounts through Maton-mediated access.

Mitigation: Users should grant access only when comfortable with that account access and should confirm every campaign, ad, audience, or deletion change before it runs.

Risk: Long-lived API keys or exposed MATON_API_KEY values can broaden credential exposure.

Mitigation: Prefer OAuth, avoid exposing MATON_API_KEY, and rely on the credential handling guidance in the skill.

Risk: Multiple Maton or Snapchat connections can make the target account ambiguous.

Mitigation: Pin the intended connection when multiple accounts exist before making API calls.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Snapchat Ads API Introduction](https://developers.snap.com/api/marketing-api/Ads-API/introduction)
- [Snapchat Ads API Patterns](https://developers.snap.com/api/marketing-api/Ads-API/api-patterns)
- [Snapchat Campaign Management](https://developers.snap.com/api/marketing-api/Ads-API/campaigns)
- [Snapchat Creative Management](https://developers.snap.com/api/marketing-api/Ads-API/creatives)
- [Snapchat Targeting](https://developers.snap.com/api/marketing-api/Ads-API/targeting)
- [Snapchat Ads Gallery API](https://developers.snap.com/api/marketing-api/Ads-Gallery-Api/using-the-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and user confirmation before connection creation or write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
