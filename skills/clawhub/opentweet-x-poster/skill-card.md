## Description: <br>
Post to X (Twitter) using the OpenTweet API to create tweets, schedule posts, publish threads and articles, upload media, manage evergreen queues, search and repurpose inspiration, run human-approved DM outreach, and read analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[petricbranko](https://clawhub.ai/user/petricbranko) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to manage connected X accounts through OpenTweet, including drafting, scheduling, publishing, article workflows, media generation, evergreen queues, analytics, and lead outreach. It requires an OpenTweet API key and should be used with review before irreversible publishing or outreach actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The OpenTweet API key can manage a connected X account, including publishing, scheduling, deleting, analytics access, media handling, and campaign workflows. <br>
Mitigation: Install only for accounts where this level of access is acceptable, verify the connection and limits before actions, and review posts, articles, media, schedules, analytics, evergreen settings, and campaign data before approval. <br>
Risk: Published posts and articles can be difficult or impossible to fully undo, and batch actions can affect many posts at once. <br>
Mitigation: Ask for explicit user confirmation before publishing, bulk scheduling, or looping publish calls; create drafts or scheduled posts first when practical and report real API response IDs and statuses. <br>
Risk: AI-generated or repurposed content and DM outreach can create reputational, compliance, or platform-policy risk if sent without review. <br>
Mitigation: Keep generated content in draft until reviewed, require human approval for each DM lead, respect opt-outs, and avoid attempts to bypass pacing or outreach caps. <br>
Risk: Uploaded or generated media, drafts, schedules, analytics, and campaign data may be stored or processed by OpenTweet. <br>
Mitigation: Avoid sending sensitive content unless OpenTweet processing is acceptable for the account and organization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/petricbranko/skills/opentweet-x-poster) <br>
- [OpenTweet OpenClaw feature page](https://opentweet.io/features/openclaw-twitter-posting) <br>
- [OpenTweet API documentation](https://opentweet.io/api/v1/docs) <br>


## Skill Output: <br>
**Output Type(s):** [api calls, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP request examples and JSON response handling.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENTWEET_API_KEY and user review for publishing, bulk scheduling, AI-generated content, and DM lead approval.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
