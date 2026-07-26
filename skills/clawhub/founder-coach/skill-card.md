## Description: <br>
AI-powered startup mindset coach that helps founders upgrade their thinking patterns, track mental model progress, and set weekly challenges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[goforu](https://clawhub.ai/user/goforu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External founders use this skill as a local coaching assistant for mindset reflection, Socratic questioning, weekly challenge setting, and progress reports. It is intended to help founders recognize thinking patterns and apply startup mental models, not to provide specific business advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read private PhoenixClaw journals and profile data and save sensitive founder coaching observations. <br>
Mitigation: Confirm PhoenixClaw integration before use, review the configured read and write paths, and establish how stored coaching observations can be reviewed, disabled, or deleted. <br>
Risk: Weekly report generation and cron-based use can persist recurring reflections without enough user awareness. <br>
Mitigation: Enable scheduled reports only after explicit user confirmation and make the generated weekly report location visible before recurring use. <br>
Risk: Startup coaching output can influence business decisions even though the skill is designed not to provide specific business advice. <br>
Mitigation: Treat coaching responses as reflection prompts and require independent review before acting on strategy, pricing, hiring, financing, or market-selection decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/goforu/skills/founder-coach) <br>
- [User Config](references/user-config.md) <br>
- [Profile Evolution](references/profile-evolution.md) <br>
- [Onboarding Process](references/onboarding.md) <br>
- [Weekly Challenge System](references/weekly-challenge.md) <br>
- [Weekly Report Generation Guide](references/weekly-report.md) <br>
- [PhoenixClaw Integration Guide](references/phoenixclaw-integration.md) <br>
- [First Round PMF Levels Framework](references/mental-models/pmf-levels.md) <br>
- [4Ps Framework: Getting Unstuck](references/mental-models/4ps-framework.md) <br>
- [NFX Mental Models for Founders](references/mental-models/nfx-models.md) <br>
- [Anti-Pattern Detection Guide: Excuse Thinking](references/anti-patterns/excuse-thinking.md) <br>
- [Anti-Pattern Detection Guide: Fear-Driven](references/anti-patterns/fear-driven.md) <br>
- [Anti-Pattern Detection Guide: Founder Trap](references/anti-patterns/founder-trap.md) <br>
- [Perfectionism](references/anti-patterns/perfectionism.md) <br>
- [Priority Chaos](references/anti-patterns/priority-chaos.md) <br>
- [Comfort Zone Trap](references/anti-patterns/comfort-zone.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown coaching responses, Obsidian-compatible Markdown files, and YAML configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local founder profile and weekly report files; PhoenixClaw access is optional and read-oriented when configured.] <br>

## Skill Version(s): <br>
0.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
