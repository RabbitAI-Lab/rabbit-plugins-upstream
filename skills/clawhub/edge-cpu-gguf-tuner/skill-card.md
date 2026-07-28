## Description: <br>
Tune llama.cpp GGUF inference on CPU-only and edge machines with low core counts and constrained memory for better tokens-per-second performance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to benchmark and tune llama.cpp GGUF model inference on CPU-only VPS, container, SBC, sandbox, or other edge environments. It helps select practical CPU settings for threads, flash attention, KV cache type, batch size, quantization, and runtime validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested build, benchmark, and generation commands can consume noticeable local CPU and memory. <br>
Mitigation: Run the commands only in a llama.cpp workspace with trusted models and monitor resource use on constrained machines. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and benchmark settings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Focuses on local llama.cpp CPU benchmarking and tuning for trusted GGUF models.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
