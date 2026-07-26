## Description: <br>
Decode an error message or stack trace into a plain-English cause, the exact fix, and how to prevent it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn error messages, stack traces, and crash output into a concise diagnosis with the likely cause, a concrete fix, and a prevention step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may infer missing language, framework, or runtime context from a partial stack trace. <br>
Mitigation: Review the labelled assumptions before applying the diagnosis or fix. <br>
Risk: Suggested code changes could be incorrect or misleading if the original error context is incomplete. <br>
Mitigation: Review and test proposed code changes before applying them to a production codebase. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/error-decoder) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/error-decoder.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Guidance] <br>
**Output Format:** [Structured Markdown with code snippets when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Labels assumptions when context is inferred from a partial error or stack trace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
