## Description: <br>
Tunes llama.cpp GGUF inference on CPU-only or constrained edge machines for better tokens/sec using measured benchmarking guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to benchmark and tune llama.cpp GGUF model inference on CPU-only VPS, container, single-board, sandbox, or other low-resource edge environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Benchmark and build commands can consume significant CPU and RAM on constrained systems. <br>
Mitigation: Run commands in the intended llama.cpp environment, review them before execution, and monitor system resources during tests. <br>
Risk: Tuning guidance may not match every model, hardware profile, or runtime build. <br>
Mitigation: Validate recommendations with local benchmarks and compare baseline and tuned runs before deployment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and benchmark parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no files, APIs, credentials, or tool integrations are produced by the skill itself.] <br>

## Skill Version(s): <br>
1.1.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
