## Description:

Helps agents manage Snapchat advertising accounts, campaigns, creatives, audiences, and performance through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Advertisers and marketing teams use this skill to inspect Snapchat ad performance and manage ad accounts, campaigns, targeting, and related advertising assets. With explicit approval, they can also set up Maton-hosted functions and triggers for automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton access to a Snapchat advertising account can enable consequential advertising changes.

Mitigation: Start with read and list calls, and obtain explicit approval before each write or automation.

Risk: Trigger destinations outside Maton can receive data from automated events.

Mitigation: Use third-party destinations only when the user controls the host and understands what data will be sent.

Risk: Event watching with --exec runs a local handler on event data.

Mitigation: Use --exec only after reviewing the handler script and obtaining separate approval.

## Reference(s):

- [ClawHub Snapchat skill](https://clawhub.ai/byungkyu/skills/snapchat)
- [Maton homepage](https://maton.ai)
- [Snapchat Ads API introduction](https://developers.snap.com/api/marketing-api/Ads-API/introduction)
- [Snapchat campaign management](https://developers.snap.com/api/marketing-api/Ads-API/campaigns)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Snapchat connection through Maton.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
