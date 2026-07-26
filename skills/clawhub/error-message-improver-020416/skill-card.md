## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague errors into clearer messages that explain what failed, why it failed, and what to do next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and affected users use this skill to convert unclear application errors into actionable troubleshooting guidance, reusable checklists, workflows, templates, analysis, code changes, or decision support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated code changes or revised production error handling could introduce incorrect or misleading behavior if applied without review. <br>
Mitigation: Review generated changes before deployment and validate revised messages against the affected workflow, expected failure modes, and support criteria. <br>
Risk: Troubleshooting output may depend on incomplete user-provided context. <br>
Mitigation: State assumptions and required inputs, ask only for missing details that materially change the result, and include a short verification note. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-020416) <br>
- [Error Messages Topic](https://segmentfault.com/t/error-messages) <br>
- [Dart SDK issue: unawaited should support FutureOr](https://github.com/dart-lang/sdk/issues/63818) <br>
- [SegmentFault troubleshooting example](https://segmentfault.com/q/1010000004886164/a-1020000004886445) <br>
- [Hacker News discussion: Ghostel.el](https://news.ycombinator.com/item?id=48905348) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, templates, and concise verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, limits, required inputs, and remaining risks when relevant.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
