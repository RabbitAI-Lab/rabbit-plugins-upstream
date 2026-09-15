## Description:

Use when designing, configuring, or implementing applications targeting the Google Gemma 4 model family, including model architecture selection, Thinking Mode formatting, function calling schemas, multimodal audio and vision pipelines, and deployment reference patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johngreenfield](https://clawhub.ai/user/johngreenfield)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select Gemma 4 variants, format thinking, tool-calling, and multimodal turns, and adapt local, browser, or Vertex AI deployment examples. It is intended for developer-controlled Gemma application design and integration work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reasoning-inspector examples can expose sensitive thought-like text.

Mitigation: Use only in developer-controlled environments, do not expose raw <thought> traces to end users or logs, and route streamed output through fail-closed parsing and review.

Risk: Remote model, tokenizer, or processor downloads can introduce supply-chain risk when revisions are not pinned.

Mitigation: Pin every remote artifact to a verified immutable revision, keep trust_remote_code=False where supported, and prefer verified local directories for restricted deployments.

Risk: Vertex AI deployment examples transmit prompt payloads to Google Cloud endpoints.

Mitigation: Verify endpoint region, retention policy, and least-privilege IAM access before processing confidential, proprietary, or regulated data.

## Reference(s):

- [Gemma 4 Hardware Sizing & VRAM Matrix](artifact/references/hardware-sizing.md)
- [Gemma 4 Native Multimodal Integration (Audio & Vision)](artifact/references/multimodal.md)
- [ClawHub skill page](https://clawhub.ai/johngreenfield/skills/gemma4-dev)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code examples and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional local, browser, and Vertex AI reference patterns; examples may require environment variables and network access.]

## Skill Version(s):

1.0.4 (source: server release metadata and OpenClaw metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
