## Description: <br>
Evaluates AI skills by measuring trigger accuracy, execution completion, correctness, quality, efficiency, and safety, then producing structured reports with Bad Cases and actionable fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rivin-dong](https://clawhub.ai/user/rivin-dong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to evaluate prompt or agent skill quality before release, compare versions, diagnose underperformance, and generate improvement guidance. It is intended for structured skill testing workflows across supported agent platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trigger tests can invoke local AI platform CLIs and exercise target skills that may write files, run shell commands, call APIs, or use browser actions. <br>
Mitigation: Run evaluations in a disposable workspace or test account and require approval for mutating tool calls during target-skill execution. <br>
Risk: Evaluation outputs can store full prompts, execution transcripts, tool calls, and reports that may contain sensitive or production data if supplied during testing. <br>
Mitigation: Use mock data, avoid real secrets and production records, and review stored outputs before sharing or publishing them. <br>
Risk: Trigger probe design can affect whether the skill is activated correctly and may produce misleading precision or recall if probes are not reviewed. <br>
Mitigation: Review positive and negative trigger probes before execution and keep probe sets representative of expected use and near-miss requests. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/rivin-dong/skill-evaluation) <br>
- [Publisher profile](https://clawhub.ai/user/rivin-dong) <br>
- [Test Case Design Guide](references/test-case-design.md) <br>
- [JSON Schemas](references/schemas.md) <br>
- [Scoring Reference](references/scoring.md) <br>
- [Rubric Templates](references/rubrics.md) <br>
- [Report Presentation Format](references/report-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON evaluation artifacts, optimized SKILL.md files, and optional HTML scorecards.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates versioned evaluation directories containing plan.md, trigger-results.json, cases.json, execution-results.json, report.md, optimized-skill/SKILL.md, and summary.md.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
