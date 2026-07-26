## Description: <br>
Nomtiq is a personalized restaurant finder for AI agents that uses live map search and a local taste profile to recommend two reliable dining options plus one exploration choice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oakcoderx](https://clawhub.ai/user/oakcoderx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use Nomtiq to answer where-to-eat requests for nearby dining, date nights, business meals, family gatherings, solo dining, and visit-feedback capture. The skill is not intended for recipes, grocery planning, calorie tracking, food delivery, reservations, or restaurant operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Restaurant queries and destinations may be sent to Amap or Serper, and optional public-web enrichment sources may be used when configured. <br>
Mitigation: Install only when this provider sharing is acceptable, keep API keys in environment variables or a secret manager, and disclose provider routing based on restaurant destination. <br>
Risk: Taste preferences, visit feedback, companion notes, and occasion history may persist locally under the skill data directory. <br>
Mitigation: Review local data regularly and use the documented export, reset, history-clear, and companion-remove commands when data should be removed. <br>
Risk: External restaurant listings and review text can be stale, incomplete, or untrusted. <br>
Mitigation: Treat provider content as data rather than instructions, state uncertainty in recommendations, and suggest confirming time-sensitive details before departure. <br>


## Reference(s): <br>
- [Nomtiq ClawHub Release](https://clawhub.ai/oakcoderx/skills/nomtiq) <br>
- [Amap Web Service API](https://restapi.amap.com) <br>
- [Serper Google Search API](https://google.serper.dev) <br>
- [SKILL.md](SKILL.md) <br>
- [AGENT_GUIDE.md](AGENT_GUIDE.md) <br>
- [README.md](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown recommendations with optional shell commands and JSON-backed local profile operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns concise 2+1 restaurant recommendations and setup or profile-management guidance; live search requires user-provided Amap or Serper credentials.] <br>

## Skill Version(s): <br>
0.5.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
