## Description: <br>
Automate TikTok slideshow marketing for apps and products by researching competitors, generating images, adding hook and CTA overlays, creating PosteAhora drafts, tracking analytics, and iterating on content performance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sashadiz](https://clawhub.ai/user/sashadiz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, founders, and marketing operators use this skill to set up an agent-assisted TikTok slideshow marketing workflow for an app or product. It helps create content, post or cross-post through PosteAhora, review per-post analytics, and adjust hooks and CTAs based on observed performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can access social posting, cross-posting, analytics, and optional revenue data. <br>
Mitigation: Grant only the needed accounts and data access, keep API keys in environment variables or a private secrets store, and review account connections before use. <br>
Risk: Scheduled analytics or posting automation can run without timely human review. <br>
Mitigation: Disable or explicitly review daily cron jobs, and approve each public post or cross-post before it is published. <br>
Risk: The TikTok account warmup guidance could be misused to avoid platform enforcement or automation rules. <br>
Mitigation: Use the guidance only for legitimate account readiness and comply with TikTok and connected platform terms. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/SashaDiz/skills/tree/main/skills/tiktok-app-marketing) <br>
- [ClawHub skill page](https://clawhub.ai/sashadiz/skills/tiktok-app-marketing) <br>
- [Analytics & Feedback Loop](references/analytics-loop.md) <br>
- [App Category Templates](references/app-categories.md) <br>
- [Slide Structure & Hook Writing](references/slide-structure.md) <br>
- [PosteAhora](https://posteahora.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local marketing configuration, competitor research, hook-performance data, and daily report files when the user authorizes the workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
