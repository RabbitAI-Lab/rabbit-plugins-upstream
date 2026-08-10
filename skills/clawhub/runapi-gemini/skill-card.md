## Description:

Call the Gemini API (the Gemini 2.5 and 3 series) through RunAPI using the official OpenAI SDK or Gemini contents clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Gemini models through RunAPI, including chat, streaming completions, multimodal vision input, Google Search grounding, structured output, reasoning effort, and client configuration for OpenAI-compatible or Gemini contents APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, and other multimodal inputs are sent to RunAPI and may be routed to Gemini-related services.

Mitigation: Avoid sending secrets, private documents, or proprietary data unless that use is approved under the relevant provider agreements and data-handling requirements.

Risk: The skill depends on a valid RunAPI API key for live API requests.

Mitigation: Store API keys in environment variables such as RUNAPI_TOKEN and avoid hard-coding credentials in prompts, code, or shared configuration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-gemini)
- [RunAPI Gemini Model Page](https://runapi.ai/models/gemini)
- [RunAPI Gemini Documentation](https://runapi.ai/models/gemini.md)
- [RunAPI Google Provider Page](https://runapi.ai/providers/google.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline code blocks and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Python, TypeScript, curl, dotenv, and environment variable guidance; requires a RunAPI API key for live requests.]

## Skill Version(s):

0.2.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
