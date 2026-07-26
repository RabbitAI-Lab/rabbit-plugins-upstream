## Description: <br>
Tune llama.cpp GGUF inference on CPU-only and edge machines with 1-4 cores or low RAM for maximum tokens per second. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to benchmark and tune local llama.cpp GGUF inference on CPU-only VPS, container, single-board computer, sandbox, or other low-resource edge environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested build and benchmark commands can consume CPU and RAM or fail outside a llama.cpp workspace. <br>
Mitigation: Run commands only in an intended llama.cpp workspace, review them before execution, and monitor resource use on constrained systems. <br>
Risk: CPU tuning recommendations may not transfer to every model, llama.cpp version, or host environment. <br>
Mitigation: Benchmark one variable at a time and validate the chosen settings on the target model and hardware before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/edge-cpu-gguf-tuner) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and benchmark tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides CPU tuning recommendations for llama.cpp GGUF inference, including build, benchmark, validation, and deployment command examples.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
