## Description: <br>
AIsa Twitter API helps agents research, monitor, search, and publish OAuth-approved text or media posts on Twitter/X through the AIsa relay. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baofeng-tech](https://clawhub.ai/user/baofeng-tech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Twitter/X profiles, timelines, trends, search results, replies, quotes, lists, communities, and Spaces, then publish posts only after explicit OAuth approval. It is suited for content research, brand or competitor monitoring, watchlists, timeline analysis, and approved text or media posting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The posting client can expose the raw AISA_API_KEY in printed JSON or error output. <br>
Mitigation: Remove or redact AISA_API_KEY from command output before using the skill in logged or agent-mediated environments. <br>
Risk: Twitter/X reads, OAuth, posting, and approved media uploads are sent through the AIsa relay. <br>
Mitigation: Use the skill only when relay-based processing is acceptable, and review text and media before sending them through api.aisa.one. <br>
Risk: Posting is an external write to Twitter/X. <br>
Mitigation: Require explicit OAuth approval and wait for API confirmation before reporting that a post succeeded. <br>


## Reference(s): <br>
- [AIsa Twitter OAuth posting guide](references/post_twitter.md) <br>
- [AIsa homepage](https://aisa.one) <br>
- [AIsa relay endpoint](https://api.aisa.one) <br>
- [ClawHub skill page](https://clawhub.ai/baofeng-tech/skills/aisa-twitter-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, AISA_API_KEY, internet access to api.aisa.one, and explicit OAuth approval for posting.] <br>

## Skill Version(s): <br>
1.0.5 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
