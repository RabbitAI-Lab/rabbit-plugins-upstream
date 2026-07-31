## Description: <br>
Chinese-language customer community operations toolbox that routes users to content writing, group messaging, conversation scripts, diagnosis, local archiving, reporting, and expert review workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and operators use this skill as a Chinese-language entry point for private-domain customer operations: drafting social posts, group broadcasts, welcome and Q&A scripts, diagnosing funnel issues, saving client notes, and generating markdown reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local customer archives and reports may contain sensitive customer or business details in plaintext markdown. <br>
Mitigation: Review or redact sensitive details before saving or exporting; treat ~/.siyu/ archives and generated reports as local sensitive files. <br>
Risk: The update helper performs user-directed installation or repository synchronization steps. <br>
Mitigation: Use the update workflow only when explicitly requested and verify the repository target before running update commands. <br>
Risk: Generated marketing, group-message, and customer-response content may create compliance risk if used without review. <br>
Mitigation: Use the bundled compliance scans and review outputs for prohibited terms, overclaims, and unauthorized personal-information collection before sending or delivering content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-siyu-team) <br>
- [Project homepage](https://github.com/maojiebc/majia-siyu-team) <br>
- [GitHub releases](https://github.com/maojiebc/majia-siyu-team/releases) <br>
- [新手教程](references/新手教程.md) <br>
- [整盘怎么搭-老板版](references/整盘怎么搭-老板版.md) <br>
- [合规前置扫描](modules/siyu-pyq/references/合规前置扫描.md) <br>
- [合规前置扫描](modules/siyu-qunfa/references/合规前置扫描.md) <br>
- [合规前置扫描](modules/siyu-huashu/references/合规前置扫描.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, structured text, local markdown files, and shell commands when update or scan workflows are requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language outputs; local archive and report workflows may write plaintext markdown files under user-directed paths.] <br>

## Skill Version(s): <br>
0.8.0 (source: frontmatter, README, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
