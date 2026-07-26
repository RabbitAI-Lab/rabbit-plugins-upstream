## Description: <br>
Configure, run, and troubleshoot Xrouter, an OpenAI-compatible LLM inference router with hardware-aware classification, provider setup guidance, routing behavior, and usage dashboard instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pathemata-mathemata](https://clawhub.ai/user/pathemata-mathemata) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to set up and operate an LLM router that selects cheap, medium, or frontier providers, configures local or cloud model endpoints, and inspects routing decisions and token usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented router defaults can expose a provider-backed chat proxy and dashboard. <br>
Mitigation: Set ROUTER_API_KEY, bind HOST to localhost unless remote access is intentional, and review network exposure before running the router. <br>
Risk: Configuration files and environment variables can contain provider API keys or routing details. <br>
Mitigation: Protect .env and upstreams.json, avoid committing secrets, and restrict file access to trusted users. <br>
Risk: Prompts may be routed to cloud providers with different data handling policies. <br>
Mitigation: Avoid routing sensitive prompts to cloud providers unless their policies are acceptable for the data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/pathemata-mathemata/skills/clawhub-skill-2) <br>
- [Ollama Quickstart](https://ollama.readthedocs.io/en/quickstart/) <br>
- [vLLM OpenAI-Compatible Server](https://docs.vllm.ai/en/stable/serving/openai_compatible_server/) <br>
- [NVIDIA TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) <br>
- [trtllm-serve](https://nvidia.github.io/TensorRT-LLM/1.0.0rc2/commands/trtllm-serve.html) <br>
- [llama.cpp](https://github.com/ggml-org/llama.cpp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local and cloud provider setup steps, environment variable guidance, request examples, and dashboard or usage endpoints.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
