## Description: <br>
Evaluate one or more prompts with an evidence-based static benchmark covering general quality, structure and format, few-shot examples, safety and robustness, target-model compatibility, and cross-model portability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, prompt engineers, and agent builders use this skill to statically score, audit, compare, and improve prompts before relying on them in production workflows. It helps separate general prompt quality from target-model compatibility and marks dynamic runtime metrics as not measured unless runtime evidence is supplied. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompt content provided for benchmarking will be read and analyzed by the agent workflow. <br>
Mitigation: Only provide prompts and related files that the agent is allowed to inspect, and handle sensitive prompt content according to the deployment environment's data policy. <br>
Risk: Static scores and compatibility predictions can be mistaken for measured runtime performance. <br>
Mitigation: Keep static findings separate from dynamic metrics, label runtime metrics as not run unless tests were actually executed, and run representative dynamic evaluations before relying on performance claims. <br>
Risk: Deterministic lint findings are heuristic leads and may overstate or miss semantic issues. <br>
Mitigation: Confirm lint findings against the prompt text and use the bundled scoring rubric before treating a finding as final. <br>


## Reference(s): <br>
- [Model compatibility assessment](artifact/references/model-compatibility.md) <br>
- [Report schema](artifact/references/report-schema.md) <br>
- [Static Prompt Benchmark scoring rubric](artifact/references/scoring-rubric.md) <br>
- [Prompt Benchmark ClawHub page](https://clawhub.ai/margaretzybgl/skills/prompt-benchmark) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown report or JSON report with optional inline shell command for deterministic linting] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Static assessment only; dynamic metrics are reported as not run unless runtime evidence is supplied.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
