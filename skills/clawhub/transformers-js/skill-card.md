## Description: <br>
Transformers.js helps developers run machine-learning models directly in JavaScript and TypeScript across browser and server runtimes for NLP, vision, audio, and multimodal tasks using WebGPU or WASM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huggingface](https://clawhub.ai/user/huggingface) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build JavaScript or TypeScript applications that load, configure, cache, and run Hugging Face Transformers.js pipelines for text, vision, audio, and multimodal workloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Examples may download remote models or dependencies and may not be local-only by default. <br>
Mitigation: Pin or self-host dependencies and models for sensitive environments, disable remote models when needed, and use cached or local assets for offline deployments. <br>
Risk: Examples may handle private URLs, prompts, tokens, or other sensitive data during model loading or inference. <br>
Mitigation: Avoid passing secrets or private URLs through examples, protect Hugging Face tokens, and apply normal privacy review before using real data. <br>
Risk: The Express API sample is illustrative and needs production controls before deployment. <br>
Mitigation: Add authentication, rate limiting, input validation, monitoring, and deployment-specific API protections before exposing any service. <br>


## Reference(s): <br>
- [ClawHub Transformers.js Skill](https://clawhub.ai/huggingface/skills/transformers-js) <br>
- [Transformers.js GitHub Repository](https://github.com/huggingface/transformers.js) <br>
- [Transformers.js Examples Repository](https://github.com/huggingface/transformers.js-examples) <br>
- [Hugging Face Transformers.js Models](https://huggingface.co/models?library=transformers.js&sort=trending) <br>
- [Configuration Reference](references/CONFIGURATION.md) <br>
- [Caching Reference](references/CACHE.md) <br>
- [Pipeline Options Reference](references/PIPELINE_OPTIONS.md) <br>
- [ModelRegistry Reference](references/MODEL_REGISTRY.md) <br>
- [Text Generation Guide](references/TEXT_GENERATION.md) <br>
- [Transformers.js Code Examples](references/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JavaScript, TypeScript, and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes browser and server-runtime examples for model selection, pipeline usage, caching, WebGPU/WASM configuration, and cleanup.] <br>

## Skill Version(s): <br>
1.0.10 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
