## Description:

Diagnoses slow, rejected, or truncated local Ollama calls using LLMxRay's read-only tools and suggests fixes for caching, context, and memory issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lognebudo](https://clawhub.ai/user/lognebudo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect their own local Ollama turns, identify prompt-cache, context-window, speed, and VRAM issues, and assess whether suggested changes helped.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LLMxRay can observe prompts and request metadata sent through its local observe port.

Mitigation: Route only calls you are comfortable exposing to the local diagnostic tool.

Risk: The documented npx startup commands do not pin the npm package version.

Mitigation: Pin the llmxray npm package version before running those commands when reproducibility matters.

## Reference(s):

- [LLMxRay project homepage](https://github.com/LogneBudo/llmxray)
- [Diagnose Ollama Calls on ClawHub](https://clawhub.ai/lognebudo/skills/llmxray-diagnose-ollama-calls)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text findings, measurements, and suggested fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings may include severity labels and per-turn performance metrics.]

## Skill Version(s):

0.8.9 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
