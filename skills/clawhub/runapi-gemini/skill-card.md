## Description: <br>
Enables agents to call Gemini models through RunAPI using OpenAI-compatible chat completions or Gemini contents clients for chat, streaming, multimodal input, Google Search grounding, structured output, and reasoning-effort workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to connect existing OpenAI or Gemini client code to Gemini models through RunAPI, including streaming, multimodal, grounding, structured-output, and model-list workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, images, files, and other request content may be sent to an external RunAPI-backed Gemini service. <br>
Mitigation: Avoid sending secrets, regulated data, or confidential business material unless that data sharing is approved for the use case. <br>
Risk: Long Gemini generations can keep an agent waiting on a blocking response. <br>
Mitigation: Use streaming for longer responses as directed by the skill guidance. <br>


## Reference(s): <br>
- [RunAPI Gemini model documentation](https://runapi.ai/models/gemini.md) <br>
- [RunAPI Gemini model page](https://runapi.ai/models/gemini) <br>
- [RunAPI Google provider documentation](https://runapi.ai/providers/google.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks, API request examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces integration guidance for RunAPI-backed Gemini requests; the skill itself does not execute hidden commands or perform destructive actions.] <br>

## Skill Version(s): <br>
0.2.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
