## Description: <br>
inference-aiops helps agents observe and operate GPU inference serving clusters across vLLM, Ray Serve, SGLang, and TGI, including latency root-cause analysis, health checks, scaling, drain, model lifecycle, and cost-per-token workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to investigate inference latency, inspect serving health and GPU usage, manage Ray Serve deployments, and perform governed operational changes on vLLM-backed inference clusters. It is also useful for observe-only SGLang and TGI health, inventory, queue, and latency analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform production-impacting inference-cluster writes without a built-in read-only mode or approval gate. <br>
Mitigation: Install it only in environments where network access and credentials are scoped to the operations allowed for the agent; for observe-only use, restrict access to read and metrics endpoints. <br>
Risk: High-risk operations such as scale-to-zero, drain, undeploy, redeploy, replica restart, LoRA unload, and model sleep can interrupt live service. <br>
Mitigation: Use dry-run previews where available, require explicit operator intent in the calling workflow, and confirm current traffic or queue state before executing disruptive writes. <br>
Risk: Credential exposure could grant access to vLLM or Ray control planes. <br>
Mitigation: Protect ~/.inference-aiops, prefer the encrypted secrets store, avoid legacy plaintext token environment variables, and scope bearer tokens to the minimum required endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/inference-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Inference-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown, shell commands, configuration snippets, and structured tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide calls that read metrics or perform state-changing operations against configured inference endpoints.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
