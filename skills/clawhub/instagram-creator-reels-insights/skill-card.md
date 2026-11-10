## Description:

Review recent public Instagram Reels from one or more creators. Get daily or weekly insights with source links, based on available transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apismith-labs](https://clawhub.ai/user/apismith-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and social media teams use this skill to review recent Reels from specified public Instagram creators, compare transcript-supported themes, and develop source-linked content ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network capability was detected, and the host runtime's permissions were not verified.

Mitigation: Confirm Apify availability and authorization through the selected host before analysis; process only user-specified public accounts and never share credentials in chat.

Risk: Discovery and transcript processing can generate usage under the user's Apify account; the per-creator processing limit does not cap usage or cost.

Mitigation: Review current usage in the Apify Console and set a per-creator processing limit for each report.

## Reference(s):

- [Instagram Creator Reels Insights project README](https://github.com/apismith-labs/instagram-ai-agent-skills#instagram-creator-reels-insights)
- [OpenClaw setup guide](https://github.com/apismith-labs/instagram-ai-agent-skills/blob/main/docs/platforms/openclaw.md#set-up-the-apify-plugin)
- [Apify OpenClaw plugin README](https://github.com/apify/apify-openclaw-plugin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Source-linked Markdown reports and content suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creator-by-creator daily or weekly results, with transcript-based observations and coverage stated as partial or unknown when needed.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
