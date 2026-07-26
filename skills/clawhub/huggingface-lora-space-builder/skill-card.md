## Description: <br>
Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA, including pipeline selection, tailored UI design, model-card settings, ZeroGPU deployment, and private publishing by default. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huggingface](https://clawhub.ai/user/huggingface) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and ML practitioners use this skill to turn a Hugging Face LoRA into a tailored Gradio Space, with guidance for selecting the correct base pipeline, writing Space files, and publishing a private demo. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may require a write-capable Hugging Face token and may reuse it as a Space secret. <br>
Mitigation: Prefer an existing secure Hugging Face login or a fine-grained token limited to the target repo or Space, avoid long-lived write tokens in chat, and store tokens as Space secrets only when needed for private or gated models. <br>
Risk: Generated Space code can include dependencies, git installs, external scripts, or secret handling that affect user security. <br>
Mitigation: Review generated app.py, requirements.txt, and README.md before publishing, with particular attention to dependencies, external CDN scripts, and HF_TOKEN handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huggingface/skills/huggingface-lora-space-builder) <br>
- [Adapting the demo to the specific LoRA](references/adapting-to-the-lora.md) <br>
- [Tasks: per-task baseline UI patterns](references/tasks.md) <br>
- [ZeroGPU and publishing](references/zerogpu-and-publishing.md) <br>
- [Creative mode: custom HTML/JS UIs in Gradio](references/creative-mode.md) <br>
- [Qwen-Image and Qwen-Image-Edit reference](references/base-models/qwen-image.md) <br>
- [LTX reference](references/base-models/ltx.md) <br>
- [Krea 2 reference](references/base-models/krea-2.md) <br>
- [Gradio documentation](https://www.gradio.app/docs) <br>
- [Hugging Face Spaces GPU documentation](https://huggingface.co/docs/hub/spaces-gpus#community-gpu-grants) <br>
- [Diffusers repository](https://github.com/huggingface/diffusers) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python, shell, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Space file contents and publishing steps; may guide Hugging Face Hub actions when the user approves.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
