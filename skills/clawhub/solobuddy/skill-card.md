## Description: <br>
Build-in-public companion for indie hackers that supports content workflows, Twitter engagement, and project soul creation as a living assistant rather than a tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[humanji7](https://clawhub.ai/user/humanji7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Indie hackers and build-in-public creators use SoloBuddy to manage content ideas, draft posts, review Twitter engagement opportunities, create project personalities from documentation, and receive activity-based prompts while staying in control of publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documented publishing actions can commit and push local content from the configured data folder. <br>
Mitigation: Use a dedicated SoloBuddy data folder, keep secrets and unrelated files out of it, and inspect diffs before any publish action. <br>
Risk: The optional Twitter monitor can run background automation and use Twitter session credentials. <br>
Mitigation: Enable monitoring only after reviewing the scripts, account access, schedule, and stop procedure; avoid placing Twitter session tokens in shell startup files. <br>
Risk: Generated posts and engagement drafts may be inaccurate, off-voice, or unsuitable for publication. <br>
Mitigation: Review all generated content and suggested comments before saving or publishing. <br>


## Reference(s): <br>
- [SoloBuddy ClawHub skill page](https://clawhub.ai/humanji7/skills/solobuddy) <br>
- [SoloBuddy README](artifact/README.md) <br>
- [Twitter Content Expert module](artifact/modules/twitter-expert.md) <br>
- [Twitter Engagement Monitor module](artifact/modules/twitter-monitor.md) <br>
- [Content Generation Guidelines](artifact/prompts/content.md) <br>
- [Voice Profiles](artifact/prompts/profile.md) <br>
- [Soul Wizard](artifact/references/soul-wizard.md) <br>
- [ClawdBot](https://clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands, JSON snippets, and generated content drafts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write drafts, backlog entries, session logs, project-soul JSON, and activity data under the configured SoloBuddy data path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
