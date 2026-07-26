## Description: <br>
Codex Review scans recent local Codex sessions, workspace artifacts, skills, automation tasks, and token records to generate a local HTML usage review with prompt diagnostics and next-week action guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joe-yyy](https://clawhub.ai/user/joe-yyy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and frequent Codex users use this skill to review recent Codex activity, understand time and token patterns, diagnose prompt gaps, and identify reusable workflows. It is useful for weekly usage reviews, project retrospectives, and local AI collaboration habit checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads recent Codex history and workspace artifact metadata, which can include project names, relative paths, usage patterns, and prompt-quality observations. <br>
Mitigation: Run it only in workspaces where local usage review is acceptable, keep generated reports in a private location, and delete reports that should not be retained. <br>
Risk: Generated reports can expose sensitive context to anyone with access to the report files, even though the artifact states reports stay local. <br>
Mitigation: Review report contents before sharing, avoid publishing generated HTML or scan JSON, and rely on the skill's redaction guidance for prompts, secrets, tokens, and unnecessary absolute paths. <br>
Risk: Active time and token totals are estimates from available local records and may be incomplete when records are missing or corrupted. <br>
Mitigation: Treat totals as directional review signals and use the troubleshooting guide to expand the time range or diagnose missing token records when numbers look incomplete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/joe-yyy/skills/codexreview) <br>
- [Publisher profile](https://clawhub.ai/user/joe-yyy) <br>
- [Project grouping rules](references/project-grouping.md) <br>
- [HTML report design guide](references/report-design.md) <br>
- [Troubleshooting guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Local HTML report, JSON scan data, and concise Markdown conversation summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated reports stay local according to the artifact; token totals and active time are estimates from local records.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
