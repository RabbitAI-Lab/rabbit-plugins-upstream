## Description: <br>
Use to generate World Cup football conversation kits from standardized match input and notification retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vivalavida-say-hi](https://clawhub.ai/user/vivalavida-say-hi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill to prepare concise World Cup football match conversation kits for group chats, in-person viewing, social posts, and selected discussion modules. It helps confirm match context, collect public Chinese sports-source signals, and optionally summarize relevant notification signals when the user requests fan-group or mobile-notification context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query recent mobile notifications when notification or fan-group context is requested. <br>
Mitigation: Use explicit notification files or tightly scoped groups, apps, keywords, and time ranges; review any notification-derived content before sharing. <br>
Risk: Public-source crawl results are advisory because the bundled crawler disables HTTPS verification. <br>
Mitigation: Cross-check important match facts with public web sources or official sources before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vivalavida-say-hi/skills/yoooclaw-world-cup-match-talk-scene-en) <br>
- [Template: Understand this game in 30 seconds](artifact/references/template-30s.md) <br>
- [Template: The main highlights of this game](artifact/references/template-main-points.md) <br>
- [Template: What are everyone talking about during this game?](artifact/references/template-discussion.md) <br>
- [Template: Pretentious words for this game](artifact/references/template-talk-lines.md) <br>
- [Template: Generate the Moments copywriting for this ball](artifact/references/template-social-post.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown conversation kit with optional inline shell commands and short reusable social/chat copy] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include facts, public-opinion summaries, tactical inferences, uncertainty labels, and notification-derived talking points when supported by user-provided or freshly queried notification data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
