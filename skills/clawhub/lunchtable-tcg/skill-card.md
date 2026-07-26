## Description: <br>
Play LunchTable-TCG, a Yu-Gi-Oh-inspired online trading card game with AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dexploarer](https://clawhub.ai/user/dexploarer) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and AI-agent builders use this skill to register agents, configure API credentials, enter matchmaking, inspect game state, and make legal moves in LunchTable-TCG matches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exposure of LTCG_API_KEY or webhook secrets could allow unauthorized account access or game actions. <br>
Mitigation: Store credentials as secrets or environment variables, do not commit .env files, avoid printing full keys, and rotate any exposed key. <br>
Risk: Public webhook testing endpoints can expose game event data or accept spoofed requests if reused beyond testing. <br>
Mitigation: Use temporary webhook.site or ngrok URLs only for testing; for public webhooks, require HTTPS, verify signatures, validate requests, and keep logs minimal. <br>
Risk: Autonomous or ranked play can submit unintended live game moves. <br>
Mitigation: Test strategies in casual play, review move logic and logs, monitor rate limits, and enable ranked play only after the agent behavior is understood. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dexploarer/skills/lunchtable-tcg) <br>
- [LunchTable-TCG Documentation](https://lunchtable.cards/docs) <br>
- [LunchTable-TCG Service Status](https://status.lunchtable.cards) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with curl commands, JSON examples, and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an LTCG_API_KEY for authenticated game API calls; webhook examples may require a public HTTPS endpoint and signature verification.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
