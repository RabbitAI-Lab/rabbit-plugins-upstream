## Description: <br>
Complete Open WebUI API integration for managing LLM models, chat completions, Ollama proxy operations, file uploads, knowledge bases (RAG), image generation, audio processing, and pipelines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0x7466](https://clawhub.ai/user/0x7466) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to interact with configured Open WebUI instances through REST APIs for model listing, chat completions, file upload, RAG knowledge management, image and audio operations, and Ollama proxy commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-chosen prompts, files, and model-management requests to the configured Open WebUI instance. <br>
Mitigation: Use a local or trusted HTTPS Open WebUI instance and review requests before sending sensitive prompts or files. <br>
Risk: Remote RAG workflows can upload private files to the configured Open WebUI service. <br>
Mitigation: Confirm that files are intended for upload and avoid sending confidential content to untrusted or remote instances. <br>
Risk: Model deletion and large model pulls can cause data loss, long runtime, bandwidth use, or storage consumption. <br>
Mitigation: Confirm destructive model operations and large downloads before execution. <br>
Risk: The skill uses an Open WebUI API token for authenticated requests. <br>
Mitigation: Keep the token out of logs and prefer scoped, revocable credentials where the Open WebUI deployment supports them. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an Open WebUI URL and bearer token supplied through environment variables or explicit parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
