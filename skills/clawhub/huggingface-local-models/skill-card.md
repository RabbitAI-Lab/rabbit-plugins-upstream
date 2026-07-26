## Description: <br>
Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. Covers finding GGUFs, quant selection, running servers, exact GGUF file lookup, conversion, and OpenAI-compatible local serving. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huggingface](https://clawhub.ai/user/huggingface) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to find llama.cpp-compatible GGUF models on Hugging Face, choose quantization for their hardware, and prepare local llama-cli or llama-server commands. It also supports exact GGUF file lookup, fallback conversion guidance, and OpenAI-compatible local serving smoke tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Model or quantization choices may be unsuitable for the user's hardware or quality needs. <br>
Mitigation: Use the Hugging Face local-app recommendation and tree API first, then apply the bundled quantization and hardware guidance when a direct recommendation is unavailable. <br>
Risk: Generated shell commands may download large model files, authenticate to gated repositories, convert model weights, or start a local server. <br>
Mitigation: Review commands before execution, authenticate only when the selected repository requires it, and confirm repository names, GGUF filenames, ports, and launch flags match the intended local workflow. <br>


## Reference(s): <br>
- [Hub Discovery Workflow](references/hub-discovery.md) <br>
- [GGUF Quantization Guide](references/quantization.md) <br>
- [Hardware Acceleration](references/hardware.md) <br>
- [llama.cpp](https://github.com/ggml-org/llama.cpp) <br>
- [Hugging Face GGUF and llama.cpp documentation](https://huggingface.co/docs/hub/gguf-llamacpp) <br>
- [Hugging Face Local Apps documentation](https://huggingface.co/docs/hub/main/local-apps) <br>
- [Hugging Face Local Agents documentation](https://huggingface.co/docs/hub/agents-local) <br>
- [GGUF converter Space](https://huggingface.co/spaces/ggml-org/gguf-my-repo) <br>
- [ClawHub skill page](https://clawhub.ai/huggingface/skills/huggingface-local-models) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with URLs and inline bash, text, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model repository names, quantization labels, GGUF filenames, hardware-specific launch flags, and local server test requests.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
