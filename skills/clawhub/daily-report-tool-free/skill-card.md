## Description: <br>
Generates Markdown daily report drafts from user-supplied dates, highlights, and blockers and writes them to a reports directory for personal work tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual users use this skill to turn daily work inputs into a consistent Markdown report with highlights, blockers, status, and next-action information. It is intended for lightweight personal work tracking rather than team reporting or advanced analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local command and search tools for a simple report-writing task. <br>
Mitigation: Review proposed commands before execution and limit file inspection to the intended report workspace. <br>
Risk: The skill includes credential and environment-check guidance that could expose unrelated local secrets. <br>
Mitigation: Do not allow scans of unrelated environment variables or secret stores; provide only the inputs needed for the report. <br>
Risk: Callback URLs or external APIs could receive report content if enabled by the user. <br>
Mitigation: Use local report generation by default and enable callbacks or external API delivery only after confirming the destination and content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/daily-report-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report draft plus structured JSON status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a dated report under reports/ when the agent has file-system permission.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
