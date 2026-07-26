## Description: <br>
Generates MP3 speech with OpenAI TTS through RunAPI for one-off CLI requests and production SDK integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to generate synchronous MP3 speech with OpenAI TTS models through RunAPI. It guides one-off generation with the RunAPI CLI and production application integration through target-language SDKs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RunAPI requests, generated audio metadata, or generated audio URLs may pass through RunAPI-managed services. <br>
Mitigation: Use this skill only when RunAPI is an intended service dependency and review data handling requirements before sending text for speech generation. <br>
Risk: RUNAPI_API_KEY or saved CLI tokens could be exposed through shell history, logs, or committed configuration. <br>
Mitigation: Store credentials in protected environment variables or saved RunAPI configuration and avoid printing or committing token values. <br>
Risk: Using the CLI as a production integration layer can create brittle runtime behavior. <br>
Mitigation: Use target-language SDKs for application, backend, worker, library, service, or production workflow integrations. <br>


## Reference(s): <br>
- [RunAPI OpenAI TTS model overview](https://runapi.ai/models/openai-tts.md) <br>
- [RunAPI OpenAI TTS homepage](https://runapi.ai/models/openai-tts) <br>
- [tts-1 variant](https://runapi.ai/models/openai-tts/tts-1.md) <br>
- [tts-1-hd variant](https://runapi.ai/models/openai-tts/tts-1-hd.md) <br>
- [RunAPI OpenAI provider page](https://runapi.ai/providers/openai.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands, SDK package names, and request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance covers SDK integration, one-off CLI use, request fields, authentication, and generated audio result handling.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
