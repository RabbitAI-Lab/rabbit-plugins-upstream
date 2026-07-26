## Description: <br>
SZZZ Case Study Lite helps agents build a local, source-traceable Chinese civil case library from user-provided PDF, DOCX, and DOC judgment files, with deduplication, expert case summaries, master reports, Q&A, and original-text backtracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[szzzcode](https://clawhub.ai/user/szzzcode) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Legal researchers, lawyers, and agents assisting them use this skill to organize local Chinese civil judgment files into a searchable, incrementally maintained case library. It supports batch extraction, deduplication, single-case summaries, master reports, case-library Q&A, and source-text verification for user-provided materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads every supported legal document in the folder supplied by the user and writes raw text copies and reports that may contain sensitive case material. <br>
Mitigation: Point the skill only at the intended case folder, keep generated law_analysis_results outputs in an appropriate local workspace, and review outputs before sharing them. <br>
Risk: The reset command deletes the generated law_analysis_results directory for the selected project. <br>
Mitigation: Use reset only after confirming the target project path and preserving any reports or extracted text that must be retained. <br>
Risk: The security summary notes unlocked dependencies. <br>
Mitigation: Install dependencies in a controlled Python environment and review dependency updates according to the user's normal software supply-chain process. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/szzzcode/skills/szzz-case-study-lite) <br>
- [README](README.md) <br>
- [Skill Instructions](SKILL.md) <br>
- [Single-Case Analysis Prompt](prompts/analyzer-logic.md) <br>
- [Master Report Prompt](prompts/master-report-logic.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated project files under law_analysis_results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local PDF, DOCX, and DOC files; writes raw extracted text, status data, deduplication reports, individual case summaries, master_data.json, and Master_Report.md.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release metadata, README, and changelog released 2026-07-20) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
