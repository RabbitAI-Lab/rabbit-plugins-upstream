## Description: <br>
Analyzes WeRead bookshelf, reading statistics, highlights, and personal thoughts to produce reading dashboards, book analyses, cross-book connections, and exportable notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yamyeed](https://clawhub.ai/user/yamyeed) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
WeRead users and agents use this skill to turn authorized reading data into personal dashboards, focused book analysis, cross-book synthesis, reading-personality summaries, and Markdown or HTML exports. It is intended for workflows where the user explicitly requests WeRead or Weixin Reading data processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses WEREAD_API_KEY to access personal WeRead bookshelf, reading statistics, highlights, and personal thoughts. <br>
Mitigation: Install and run only when comfortable granting that access, keep the API key private, and confirm the requested data scope before analysis. <br>
Risk: Cross-book analysis can aggregate private notes and reading history beyond the minimum needed for a single-book request. <br>
Mitigation: Confirm the books and data range before cross-book analysis, and limit requests to the smallest useful scope. <br>
Risk: Generated Markdown or HTML exports may contain private notes, highlights, and reading history. <br>
Mitigation: Review generated files before sharing and confirm the file type, path, and included data before export or opening. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yamyeed/skills/weread-ai-brain) <br>
- [WeRead agent gateway](https://i.weread.qq.com/api/agent/gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, single-file HTML dashboards, Markdown exports, shell command examples, and API request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the user's WEREAD_API_KEY to read authorized WeRead data; export paths, local files, browser opening, and cross-book aggregation require user confirmation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
