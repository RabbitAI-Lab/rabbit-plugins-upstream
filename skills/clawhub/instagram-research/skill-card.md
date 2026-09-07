## Description:

Researches public Instagram profiles, posts, and Reels through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill for public Instagram profile checks, influencer vetting, competitor social audits, Reels review, and post-level engagement checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key could be exposed to an unexpected destination if CRAWLORA_API_BASE is changed to an untrusted URL.

Mitigation: Keep CRAWLORA_API_BASE unset unless the destination is fully trusted, and use a Crawlora key with the narrowest available permissions.

Risk: The helper can make authenticated Crawlora API calls beyond the documented Instagram profile, Reels, and post lookups.

Mitigation: Review commands before execution and limit use to the documented public Instagram endpoints.

Risk: Instagram data access may create policy or privacy concerns if used beyond public profile, post, and Reels data.

Mitigation: Use the skill only for public data and respect Instagram's terms and applicable policy requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/instagram-research)
- [Instagram Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are raw JSON suitable for jq or downstream analysis.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
