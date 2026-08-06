## Description:

Call the MiMo API through RunAPI using OpenAI-compatible Chat Completions or Responses clients, or Anthropic-compatible Messages clients for text generation, supported image understanding, streaming, and existing LLM client integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route MiMo model requests through RunAPI from OpenAI-compatible or Anthropic-compatible clients. It helps agents produce correct setup guidance, code examples, streaming requests, and supported image URL requests without adding unsupported fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI API keys could be exposed if copied into code or shared transcripts.

Mitigation: Keep credentials in environment variables or a secret manager and avoid embedding real tokens in generated examples.

Risk: Prompts and HTTP(S) image URLs are sent to RunAPI/MiMo when the skill is used.

Mitigation: Avoid sending sensitive prompts or image URLs unless that matches the user's data-sharing expectations.

Risk: Unsupported tools, advanced controls, document, audio, video, data URL image, or out-of-subset multimodal fields may produce rejected or misleading requests.

Mitigation: Keep requests within the documented MiMo subset and omit unverified fields such as image detail or cache control.

## Reference(s):

- [RunAPI MiMo model documentation](https://runapi.ai/models/mimo.md)
- [RunAPI MiMo homepage](https://runapi.ai/models/mimo)
- [RunAPI Xiaomi provider page](https://runapi.ai/providers/xiaomi.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-mimo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with dotenv, Python, TypeScript, and API client examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires RunAPI credentials in environment variables and stays within the verified MiMo text, streaming, and synchronous image URL subset.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
