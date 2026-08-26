## Description: <br>
Mongolian AI for Codex routes Mongolian translation, script conversion, conversation, OCR, ASR, TTS, and Word/PDF translation tasks through the Mongol AI API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youteacherasia](https://clawhub.ai/user/youteacherasia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to perform Mongolian-language translation, transcription, speech generation, OCR, composition, and document translation through a dedicated external API rather than relying on model knowledge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected text, images, audio, and documents to mongol.open-idea.net under the user's API key. <br>
Mitigation: Use it only for material approved for upload to that external service, and obtain explicit confirmation before sending confidential, regulated, credential-containing, or highly personal content. <br>
Risk: Long text, batches, files, images, audio, or agent-initiated calls can incur service charges. <br>
Mitigation: Confirm the billing basis and user intent before these operations, and refer users to the current pricing page rather than hard-coding prices. <br>
Risk: Traditional Mongolian work can be incorrect if the agent bypasses the dedicated API and relies on model knowledge. <br>
Mitigation: Route Mongolian translation, interpretation, script conversion, and generation through the documented Mongol AI endpoints, and stop when the API key or service is unavailable. <br>


## Reference(s): <br>
- [Mongol AI service homepage](https://mongol.open-idea.net) <br>
- [Mongol AI pricing](https://mongol.open-idea.net/#pricing) <br>
- [HTTP request and response contracts](references/HTTP-REQUESTS.md) <br>
- [Routing rules](references/INTERFACE-ROUTING.md) <br>
- [Behavior, privacy, cost, and retries](references/BEHAVIOR-RULES.md) <br>
- [Translation and segmentation](references/TRANSLATION.md) <br>
- [Chat and composition](references/CHAT-COMPLETIONS.md) <br>
- [OCR](references/OCR.md) <br>
- [ASR](references/ASR.md) <br>
- [TTS](references/TTS.md) <br>
- [Word and PDF translation](references/DOCUMENT-TRANSLATION.md) <br>
- [API key handling](references/API-KEY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with saved file paths for generated audio] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May append billing metadata when returned by the service; requires MONGOL_AI_SKILL_API_KEY and the bash, curl, and python3 binaries.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
