## Description: <br>
Generates structured daily report Markdown drafts from user-provided dates, highlights, and blockers, then writes them to a local reports directory for personal work records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and individual contributors use this skill to turn daily work inputs into a consistent Markdown report that records highlights, blockers, and a next action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes Markdown files locally, so report generation can create or overwrite local artifacts if paths or permissions are not reviewed. <br>
Mitigation: Run it in a workspace where writing to reports/ is expected, review generated files before sharing, and keep backups for important reports. <br>
Risk: Privacy and network behavior are not clearly bounded in the release evidence, and reports may contain confidential work details or blockers. <br>
Mitigation: Avoid entering sensitive business details, credentials, or confidential blockers unless the active agent, model provider, callbacks, and external API behavior are understood and acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/daily-report-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report file with structured JSON-style status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes daily report drafts under reports/ and may include execution status, logs, and nextAction fields.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
