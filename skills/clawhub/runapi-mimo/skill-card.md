## Description:

Call the MiMo API (mimo-v2.5-pro and mimo-v2.5) through RunAPI using OpenAI-compatible Chat Completions. Use for MiMo text generation, the verified MiMo image subset, streaming, or an existing compatibility client that needs the conditional reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure agents or compatibility clients for MiMo text generation, synchronous image-capable chat requests, and streaming through RunAPI's OpenAI-compatible Chat Completions endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI credentials could be exposed if copied into source files, prompts, or logs.

Mitigation: Keep the RunAPI key in an environment variable or secret manager and avoid hard-coding it in examples or agent configuration.

Risk: Requests could send sensitive prompts or image URLs to RunAPI outside the user's data-handling requirements.

Mitigation: Confirm that the configured base URL and the data being sent are approved before submitting MiMo requests.

## Reference(s):

- [MiMo model overview and pricing](https://runapi.ai/models/mimo.md)
- [RunAPI MiMo homepage](https://runapi.ai/models/mimo)
- [Xiaomi provider page](https://runapi.ai/providers/xiaomi.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [MiMo compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python code examples, environment variable configuration, and protocol guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve exact MiMo model IDs, use the RunAPI base URL, verify final content and usage, and stop after bounded retries.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
