## Description: <br>
Benchmark LLM model throughput by measuring tokens per second, latency, output speed, and error rate using OpenClaw auto mode or OpenAI-compatible API endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsag1](https://clawhub.ai/user/tsag1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to benchmark language model throughput before selecting or changing models. It can run a no-key OpenClaw benchmark for the current session model or call an OpenAI-compatible API endpoint for direct model comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Benchmark prompts may be sent to OpenClaw or to a user-provided OpenAI-compatible API endpoint. <br>
Mitigation: Use non-sensitive test prompts and only benchmark against trusted API URLs. <br>
Risk: API keys may be exposed if long-lived secrets are passed directly on command lines. <br>
Mitigation: Prefer short-lived credentials or local secret-handling practices that avoid persisting keys in shell history. <br>
Risk: Generated benchmark reports may be saved locally and can include model names, endpoint URLs, prompts, and error details. <br>
Mitigation: Review report contents before sharing and write outputs only to appropriate local paths. <br>
Risk: Auto mode estimates token counts and cannot cap output length, so results may be less precise for some models or prompts. <br>
Mitigation: Use API mode when precise completion-token counts or max-token controls are required, and adjust timeout or prompt length for slow models. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tsag1/skills/model-throughput-tester) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Terminal status text plus Markdown report files, with optional CSV output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include per-model and per-iteration throughput, latency, output token counts, status, and error-rate summaries.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
