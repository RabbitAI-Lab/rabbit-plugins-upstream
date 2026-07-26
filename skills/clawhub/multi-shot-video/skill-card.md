## Description: <br>
Helps an agent produce short multi-shot Runware video reels by collecting story beats, choosing an appropriate video model, and shaping model-specific prompt and request payloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creative operators, and agents use this skill to create a single video request that tells one subject's story across multiple cuts instead of generating one continuous shot or stitching clips manually. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and optional anchor images may be sent to Runware video models. <br>
Mitigation: Use only content intended for the provider request, and avoid sending sensitive or unapproved assets as prompts or anchor frames. <br>
Risk: Video generation and optional audio can incur provider charges. <br>
Mitigation: Confirm duration, model choice, anchor usage, and audio settings before submitting jobs, especially for repeated retries. <br>
Risk: Model availability and schemas can change, which may make stale model choices or field names fail. <br>
Mitigation: Resolve the live model schema before calling and mirror the current field names, duration limits, prompt caps, and async polling requirements. <br>
Risk: Multi-shot outputs may drift in subject identity or produce a single continuous take if the prompt lacks clear shot grammar. <br>
Mitigation: Use the documented shot templates, add a continuity clause, verify the rendered cuts, and retry with tighter continuity or anchor frames when needed. <br>


## Reference(s): <br>
- [Multi-shot video worked recipes](artifact/references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, api calls, configuration] <br>
**Output Format:** [Markdown guidance with JSON request examples and model-specific prompt templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include Runware videoInference payloads, shot-list prompts, anchor-frame settings, async polling guidance, and quality checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
