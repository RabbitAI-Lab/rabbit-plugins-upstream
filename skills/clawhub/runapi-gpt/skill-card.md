## Description:

Guides agents using OpenAI-compatible clients to call GPT generation and text embedding models through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure RunAPI clients and select supported requests for GPT chat, Responses, embeddings, streaming, tools, vision, or live audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model requests send prompts and other supplied data to RunAPI for processing.

Mitigation: Use this skill only when RunAPI is an approved processor; check account policies and data-retention terms before sending secrets, regulated data, or private documents.

Risk: A RunAPI API key is required for client requests.

Mitigation: Keep the key in the OPENAI_API_KEY environment variable rather than embedding it in examples or shared files.

## Reference(s):

- [GPT on RunAPI documentation](https://runapi.ai/models/gpt.md)
- [RunAPI OpenAI provider](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [GPT on RunAPI model page](https://runapi.ai/models/gpt)
- [Compatibility protocols](references/compatibility-protocols.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Request shapes and model support depend on the RunAPI endpoint and current contract.]

## Skill Version(s):

0.2.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
