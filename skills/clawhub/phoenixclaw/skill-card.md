## Description: <br>
PhoenixClaw is a passive journaling skill that scans OpenClaw session, agent, cron, and memory logs to generate Markdown journals, summaries, profile updates, timelines, growth maps, and plugin-enhanced reflections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[goforu](https://clawhub.ai/user/goforu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users use PhoenixClaw to turn daily conversations, memories, and media into personal Markdown journals and longer-term self-reflection records. It supports manual journal requests as well as scheduled nightly generation with optional plugins for domain-specific sections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read broad private session, agent, cron, and memory logs. <br>
Mitigation: Install only with explicit intent to journal from those sources, review configured read paths, and limit source access where the runtime allows. <br>
Risk: The skill can copy media and store personal or media-derived records in journal assets and profile files. <br>
Mitigation: Review the journal path, media retention expectations, profile and growth-map updates, and exclude sensitive screenshots or personal media before scheduled use. <br>
Risk: Scheduled cron operation and plugins can process personal data without a fresh prompt each time. <br>
Mitigation: Review the cron job, disable unneeded plugins, and confirm each enabled plugin's data access and journal export behavior. <br>
Risk: The release security guidance calls out shell fallbacks as an area needing review. <br>
Mitigation: Prefer a version that removes shell fallbacks, or run this skill with least-privilege filesystem permissions and inspect generated commands before deployment. <br>


## Reference(s): <br>
- [PhoenixClaw skill page](https://clawhub.ai/goforu/skills/phoenixclaw) <br>
- [User configuration](references/user-config.md) <br>
- [Cron setup](references/cron-setup.md) <br>
- [Media handling](references/media-handling.md) <br>
- [Plugin protocol](references/plugin-protocol.md) <br>
- [Obsidian format](references/obsidian-format.md) <br>
- [Profile evolution](references/profile-evolution.md) <br>
- [Skill recommendations](references/skill-recommendations.md) <br>
- [Visual design](references/visual-design.md) <br>
- [Session day audit utility](references/session-day-audit.js) <br>
- [Rolling journal script](scripts/rolling-journal.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown journals and summaries with YAML frontmatter, Obsidian-style links, configuration snippets, shell commands, and generated profile/timeline/growth files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May copy selected media into journal assets and may include plugin-generated sections when enabled.] <br>

## Skill Version(s): <br>
0.0.19 (source: skill frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
