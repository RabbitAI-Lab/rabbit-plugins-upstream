## Description: <br>
One Eval guides an agent through end-to-end benchmarking of pure-text LLMs using API or local vLLM models, benchmark selection, metric scoring, and illustrated report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericciregyz](https://clawhub.ai/user/ericciregyz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and evaluation engineers use this skill to configure, run, score, and summarize pure-text LLM benchmarks. It helps compare model performance across selected benchmarks and optional metrics while producing local evaluation outputs and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private benchmark data or prompts may be sent to third-party model API endpoints during evaluation. <br>
Mitigation: Use trusted model endpoints for sensitive evaluations and obtain approval before sending private data to external APIs. <br>
Risk: Custom metric Python files and external benchmark repositories can execute untrusted code. <br>
Mitigation: Only add custom metrics or external benchmark repositories that are trusted, reviewed, and run in a controlled project environment. <br>
Risk: Evaluation specifications can contain API keys or endpoint details. <br>
Mitigation: Keep evalspec files out of source control and avoid echoing credentials in agent responses or reports. <br>


## Reference(s): <br>
- [One Eval ClawHub release](https://clawhub.ai/ericciregyz/skills/one-eval) <br>
- [Eval Types](references/eval_types.md) <br>
- [Bench Gallery](references/bench_gallery.md) <br>
- [Metric Registry](references/metric_registry.md) <br>
- [Model Setup](references/model_setup.md) <br>
- [External Bench](references/external_bench.md) <br>
- [Report Template](references/report_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code] <br>
**Output Format:** [Markdown guidance with shell commands, YAML configuration, local report files, and optional Python metric code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local evalspec configuration, evaluation outputs, metric results, and HTML or Markdown reports; API keys should remain local and out of source control.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
