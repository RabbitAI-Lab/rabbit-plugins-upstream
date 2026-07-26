## Description: <br>
Evaluate one or more prompts with an evidence-based static benchmark covering general quality, structure and format, few-shot examples, safety and robustness, target-model compatibility, and cross-model portability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, prompt authors, and AI reviewers use this skill to score, audit, lint, compare, and diagnose prompts before relying on them in production or cross-model workflows. It produces static quality and compatibility assessments without claiming measured runtime performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read prompt files explicitly provided for analysis. <br>
Mitigation: Only provide prompts and files intended for local review, and handle sensitive prompt content according to the user's data policy. <br>
Risk: The bundled Python lint script may be executed during analysis. <br>
Mitigation: Run the script only from the reviewed artifact in a trusted local environment; server security evidence reports no hidden network calls, credential handling, persistence, or destructive behavior. <br>
Risk: Static compatibility predictions can be mistaken for measured model performance. <br>
Mitigation: Label runtime metrics such as accuracy, hallucination rate, latency, cost, and consistency as not measured unless a separate dynamic evaluation was actually run. <br>


## Reference(s): <br>
- [Scoring Rubric](references/scoring-rubric.md) <br>
- [Report Schema](references/report-schema.md) <br>
- [Model Compatibility Assessment](references/model-compatibility.md) <br>
- [Prompt Benchmark on ClawHub](https://clawhub.ai/margaretzybgl/skills/prompt-benchmark) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown report by default, with JSON report output when requested and optional inline shell commands for local linting.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Static benchmark output separates universal prompt quality from target-model compatibility and marks dynamic metrics as not run unless runtime evidence is supplied.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
