## Description: <br>
Provides guidance for building and reviewing Gradio Spaces that use Hugging Face ZeroGPU, including @spaces.GPU, quota duration, process isolation, concurrency, and CUDA dependency constraints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huggingface](https://clawhub.ai/user/huggingface) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when writing or reviewing Gradio SDK Spaces on ZeroGPU. It helps them choose @spaces.GPU patterns, duration and quota settings, process-boundary-safe data handling, concurrency-safe outputs, and CUDA dependency pins. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ZeroGPU runtime details, quotas, and supported versions can change over time. <br>
Mitigation: Verify the current Hugging Face ZeroGPU documentation before sizing workloads, setting duration values, or changing Python, Torch, and CUDA dependencies. <br>
Risk: Incorrect CUDA wheel or torch side-car pins can break Space builds or runtime imports. <br>
Mitigation: Match wheel tags to the pinned Python, CUDA, and Torch versions, and prefer documented kernels-community packages when ABI compatibility is uncertain. <br>
Risk: Concurrent ZeroGPU handlers can overwrite shared mutable state or fixed output paths. <br>
Mitigation: Keep request data out of mutable globals, use per-invocation temporary paths, and treat read-only model objects as the safe module-scope pattern. <br>


## Reference(s): <br>
- [Hugging Face ZeroGPU documentation](https://huggingface.co/docs/hub/spaces-zerogpu) <br>
- [ZeroGPU AoTI guidance](https://huggingface.co/blog/zerogpu-aoti) <br>
- [Hugging Face kernels-community](https://huggingface.co/kernels-community) <br>
- [flash-attention releases](https://github.com/Dao-AILab/flash-attention/releases) <br>
- [Concurrency Safety](references/concurrency.md) <br>
- [CUDA Dependencies on ZeroGPU](references/cuda-and-deps.md) <br>
- [How ZeroGPU duration and quota are checked](references/how-quota-works.md) <br>
- [How ZeroGPU works](references/how-zerogpu-works.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; no tools, credentials, or executable hooks are included.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
