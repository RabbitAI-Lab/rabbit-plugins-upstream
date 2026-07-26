## Description: <br>
Generate contextual follow-up suggestions after AI responses. Shows 3 clickable buttons (Quick, Deep Dive, Related) when user types "/followups". <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users use this skill to generate three contextual follow-up questions after an AI response, with button output on supported chat channels and numbered text fallback elsewhere. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recent chat context is used to generate suggestions, which can expose sensitive conversation details to the configured AI provider. <br>
Mitigation: Use the explicit /followups trigger for normal use and avoid requesting suggestions in conversations containing sensitive information. <br>
Risk: Auto-trigger mode can broaden when suggestions are generated after responses. <br>
Mitigation: Keep autoTrigger disabled unless continuous follow-up suggestions are intentionally desired. <br>
Risk: The standalone CLI can rely on API keys for external providers. <br>
Mitigation: Prefer OpenClaw-native auth for the main skill and avoid storing API keys in shell startup files when using the CLI. <br>


## Reference(s): <br>
- [Smart Follow-ups on ClawHub](https://clawhub.ai/robbyczgw-cla/skills/smart-followups) <br>
- [OpenClaw](https://openclaw.com) <br>
- [Channel Support Guide](CHANNELS.md) <br>
- [Quick Start](QUICKSTART.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or channel-native button/text suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces three categorized follow-up suggestions: Quick, Deep Dive, and Related.] <br>

## Skill Version(s): <br>
2.1.8 (source: server release evidence, SKILL.md frontmatter, changelog released 2026-03-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
