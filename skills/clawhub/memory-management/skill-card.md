## Description: <br>
Manages authorized HOT/WARM/COLD project memory for initialization, lookup, consolidation, archival, and erasure while preserving canonical registry ownership and privacy controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to initialize, query, consolidate, archive, and purge authorized project memory across sessions. It is intended for project-local working memory and must not be used to change canonical registry facts outside the owning registry workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent project memory can capture sensitive personal data, credentials, or operational details if paths and content are not controlled. <br>
Mitigation: Require explicit authorization before persistent writes, keep runtime memory out of git, and avoid storing credentials or unnecessary personal data. <br>
Risk: Cached memory can become stale or conflict with canonical registry records. <br>
Mitigation: Treat HOT/WARM/COLD notes as non-canonical, verify registry projections and live consent state before acting, and submit conflicts through the owning registry workflow. <br>
Risk: Privacy purge workflows can be misunderstood as complete deletion from history and backups. <br>
Mitigation: Report purge scope precisely, preserve only minimized tombstones where needed, and escalate full history or backup destruction to the responsible data-retention process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/memory-management) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Promotion and demotion rules](references/promotion-demotion-rules.md) <br>
- [Consolidation pass](references/consolidation-pass.md) <br>
- [Update triggers and integration](references/update-triggers-integration.md) <br>
- [Examples](references/examples.md) <br>
- [GDPR purge log template](references/gdpr-purge-log-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file path summaries and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce authorized memory file writes, archive summaries, purge records, and registry proposal or verification event references.] <br>

## Skill Version(s): <br>
19.0.0 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
