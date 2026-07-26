## Description: <br>
Maintains the Research KB team-level overview pages from an existing Gitea-backed knowledge base for scheduled OpenClaw cron runs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[myd2002](https://clawhub.ai/user/myd2002) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and team operators use this skill to inspect a Gitea-backed team knowledge base, guide evidence selection, validate overview drafts, and apply updates only to the six team-level overview pages plus catalog and maintenance status files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Gitea bot token with broad permissions could allow unintended KB writes. <br>
Mitigation: Use a dedicated bot token scoped as narrowly as practical to the intended KB repository. <br>
Risk: Untrusted payload or environment configuration could direct maintenance at the wrong repository or content set. <br>
Mitigation: Run the skill only with trusted payloads and configuration for the intended team KB. <br>
Risk: Incorrect overview drafts could publish misleading team-level KB summaries. <br>
Mitigation: Base drafts on inspection evidence, run validate-pages before apply, and review changes when maintenance decisions are uncertain. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/myd2002/skills/kb-maintenance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown drafts, JSON inspection/status files, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes are constrained to documented overview pages, catalog/index updates, and hidden maintenance status/history files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
