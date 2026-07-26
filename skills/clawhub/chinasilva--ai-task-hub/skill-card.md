## Description: <br>
AI task hub for image analysis, background removal, speech-to-text, text-to-speech, markdown conversion, and points queries. Default host path is connector-first and result-first; async poll/presentation remain compatibility or asset-delivery follow-up surfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chinasilva](https://clawhub.ai/user/chinasilva) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and host-runtime integrators use this skill to run AI media, document, retrieval, generation, and account-points tasks through AI Task Hub. It supports image analysis, cutout and matting, transcription, text-to-speech, markdown conversion, embeddings, reranking, image generation, video face generation, async polling, rendered outputs, balance checks, and ledger review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images, audio, video, documents, text inputs, and account-points requests are sent to BinaryWorks for processing. <br>
Mitigation: Use the skill only after user consent for the selected files or inputs, and avoid sensitive or regulated data unless the host clearly asks for and records approval. <br>
Risk: Account continuity depends on keeping entry_user_key private and consistently reused by the host or connector. <br>
Mitigation: Store continuity identifiers in the host or connector layer, do not expose them to end users, and retry with the same identifier after authorization. <br>
Risk: Separate connector packages may affect the deployed trust boundary. <br>
Mitigation: Review any connector package and its requested behavior before installation, especially where it manages continuity or account authorization. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chinasilva/ai-task-hub) <br>
- [Publisher Profile](https://clawhub.ai/user/chinasilva) <br>
- [AI Task Hub Homepage](https://gateway.binaryworks.app) <br>
- [Capability Reference](references/capabilities.json) <br>
- [OpenAPI Reference](references/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown, JSON, text, generated media file links, rendered asset references, and account data returned by the selected action.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some capabilities return immediate results; asset-delivery and long-running capabilities may require polling and a presentation fetch.] <br>

## Skill Version(s): <br>
3.3.14 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
