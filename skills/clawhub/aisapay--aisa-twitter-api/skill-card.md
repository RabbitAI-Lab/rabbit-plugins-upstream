## Description: <br>
Searches and reads X (Twitter): profiles, timelines, mentions, followers, tweet search, trends, lists, communities, and Spaces, and publishes posts after the user completes OAuth in the browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisapay](https://clawhub.ai/user/aisapay) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, social media operators, and autonomous agents use this skill to search Twitter/X data, inspect profiles and engagement, monitor trends or mentions, and publish approved posts or media through OAuth-backed workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish public Twitter/X posts, replies, quotes, threads, images, or videos. <br>
Mitigation: Verify the final text, media attachments, and post relationship before execution, and do not treat an authorization URL as proof that posting succeeded. <br>
Risk: Normal command output can expose the raw AISA_API_KEY. <br>
Mitigation: Treat command output and logs as sensitive, avoid sharing them, and rotate the key if it is disclosed. <br>
Risk: Selected local media files are uploaded through the AIsa relay for posting. <br>
Mitigation: Pass only intended image or video paths and review attachments before publishing. <br>
Risk: TWITTER_RELAY_BASE_URL can redirect requests to an alternate relay. <br>
Mitigation: Leave TWITTER_RELAY_BASE_URL unset unless the alternate relay is explicitly trusted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aisapay/skills/aisa-twitter-api) <br>
- [Publisher Profile](https://clawhub.ai/user/aisapay) <br>
- [Post Twitter OAuth Workflow](artifact/references/post_twitter.md) <br>
- [AIsa API Reference](https://docs.aisa.one/reference/) <br>
- [OpenClaw Homepage](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY; posting workflows may return authorization URLs, tweet IDs, tweet links, raw API responses, or error messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
