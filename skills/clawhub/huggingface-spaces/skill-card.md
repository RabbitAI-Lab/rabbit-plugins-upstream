## Description: <br>
Build, deploy, and maintain applications on Hugging Face Spaces across Gradio, Docker, Static SDKs, ZeroGPU, dedicated hardware, model loading, debugging, buckets, inference providers, and community grants. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huggingface](https://clawhub.ai/user/huggingface) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, configure, deploy, debug, and maintain Hugging Face Spaces for machine-learning demos, hosted applications, provider-backed apps, and persistent-storage workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to run Hugging Face CLI commands that create or modify Spaces, settings, secrets, buckets, hardware, and visibility. <br>
Mitigation: Confirm the target namespace, Space name, visibility, hardware, bucket, and any write operation before running proposed commands. <br>
Risk: Hugging Face write tokens or Space secrets could be exposed if pasted into prompts, files, public environment variables, or public repositories. <br>
Mitigation: Use hf auth login or Space secrets for tokens, avoid placing write tokens in prompts or committed files, and keep sensitive values out of visible environment variables. <br>
Risk: Paid hardware, storage buckets, provider-backed inference, or public posting can create cost, access, or disclosure impact. <br>
Mitigation: Check account payment capability and confirm paid resources, public bucket behavior, Space visibility, and public Community posts with the user before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huggingface/skills/huggingface-spaces) <br>
- [Hugging Face Spaces Overview](https://huggingface.co/docs/hub/spaces-overview) <br>
- [Spaces Configuration Reference](https://huggingface.co/docs/hub/spaces-config-reference) <br>
- [Docker Spaces SDK](https://huggingface.co/docs/hub/spaces-sdks-docker) <br>
- [Static Spaces SDK](https://huggingface.co/docs/hub/spaces-sdks-static) <br>
- [ZeroGPU Documentation](https://huggingface.co/docs/hub/spaces-zerogpu) <br>
- [Storage Buckets Documentation](https://huggingface.co/docs/hub/storage-buckets) <br>
- [ZeroGPU Reference](references/zerogpu.md) <br>
- [Debugging and Iteration Reference](references/debugging.md) <br>
- [Known Errors Reference](references/known-errors.md) <br>
- [Requirements Reference](references/requirements.md) <br>
- [Gradio Reference](references/gradio.md) <br>
- [Persistent Storage Reference](references/buckets.md) <br>
- [Community GPU Grants Reference](references/grants.md) <br>
- [Inference Providers Reference](references/inference-providers.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Hugging Face CLI commands, Python snippets, README frontmatter, dependency files, debugging steps, and deployment configuration.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
