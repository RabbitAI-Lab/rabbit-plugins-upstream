## Description: <br>
Debugging Log Analyser parses error logs, stack traces, and crash reports into structured root-cause diagnoses with error classification, stack-trace walkthroughs, likely causes, code-level fixes, and next debugging steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn application errors, crashes, and stack traces into actionable debugging reports and fix suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Logs and crash reports may contain secrets, tokens, customer data, or production identifiers. <br>
Mitigation: Redact sensitive values before sharing logs with an agent or using this skill. <br>
Risk: Debugging diagnoses and fix suggestions can be incomplete or incorrect when logs lack context. <br>
Mitigation: Provide the requested language, framework, environment, change history, frequency, and previous attempts, then review proposed fixes before applying them. <br>


## Reference(s): <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/debugging-log-analyser.html) <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/debugging-log-analyser) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown debugging report with structured sections, code snippets, and command examples when relevant] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes classification, stack-trace analysis, root-cause confidence, affected code path, suggested fix, next steps, and prevention guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
