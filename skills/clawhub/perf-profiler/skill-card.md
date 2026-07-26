## Description: <br>
Profile and optimize application performance when diagnosing slow code, measuring CPU and memory usage, generating flame graphs, benchmarking functions, load testing APIs, finding memory leaks, or optimizing database queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to profile applications, benchmark code and endpoints, investigate memory growth, load test APIs, and compare performance before and after changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Benchmarking and profiling examples can execute arbitrary commands or target systems the user is not authorized to test. <br>
Mitigation: Review generated commands before execution, use only code, hosts, and services you own or are authorized to test, and avoid commands derived from untrusted text. <br>
Risk: Load testing can stress services or production infrastructure. <br>
Mitigation: Avoid production targets unless formally approved, start with low concurrency and short durations, and increase load only under an authorized test plan. <br>
Risk: Profiling outputs such as heap snapshots, traces, and database plans can expose sensitive operational details. <br>
Mitigation: Review profiler artifacts before sharing, store them in approved locations, and redact secrets or sensitive data from captured outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/perf-profiler) <br>
- [hyperfine benchmarking tool](https://github.com/sharkdp/hyperfine) <br>
- [wrk load testing tool](https://github.com/wg/wrk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include benchmark commands, profiler setup steps, diagnostic code snippets, and interpretation guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
