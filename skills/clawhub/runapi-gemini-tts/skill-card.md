## Description: <br>
Generate multi-speaker speech with Gemini TTS through RunAPI, using the RunAPI CLI for one-off generation and the language SDK for application integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate multi-speaker Gemini TTS audio through RunAPI, either by issuing one-off CLI commands or by integrating the RunAPI SDK into an application or service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TTS prompts and dialogue content are processed by RunAPI and its provider. <br>
Mitigation: Review the content before submission and avoid sending data that should not be processed by those services. <br>
Risk: RunAPI credentials could be exposed if placed in prompts, source files, logs, or command history. <br>
Mitigation: Store the API key only in RUNAPI_API_KEY or trusted CLI configuration, as the skill and security guidance recommend. <br>
Risk: Using the CLI as a production integration layer can make application behavior harder to maintain. <br>
Mitigation: Use the SDK integration path for applications, services, workers, and production workflows; reserve the CLI path for one-off generation, smoke tests, and debugging. <br>


## Reference(s): <br>
- [Gemini TTS model overview, pricing, and rate limits](https://runapi.ai/models/gemini-tts.md) <br>
- [RunAPI Gemini TTS homepage](https://runapi.ai/models/gemini-tts) <br>
- [Google provider comparison](https://runapi.ai/providers/google.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and SDK package names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to create JSON request files and use RUNAPI_API_KEY or saved CLI configuration for authentication.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
