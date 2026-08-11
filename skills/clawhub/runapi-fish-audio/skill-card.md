## Description:

Generate MP3 or WAV speech with Fish Audio through RunAPI for one-off speech generation or application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate text-to-speech audio with Fish Audio through RunAPI, either as one-off CLI requests or through language-specific SDK integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed if copied into prompts, request files, shell history, or logs.

Mitigation: Use RUNAPI_API_KEY or trusted RunAPI CLI configuration, and avoid embedding credentials in generated code or request payloads.

Risk: Speech text, reference voice samples, transcripts, and generated audio URLs may be processed or stored by RunAPI-managed services.

Mitigation: Avoid sending sensitive text, voice samples, or transcripts unless the user accepts RunAPI-managed processing and storage for that data.

Risk: Using the CLI as a production integration layer can create brittle application behavior.

Mitigation: Use the target-language RunAPI SDK for application or production integration, and reserve the CLI for one-off generation, smoke tests, and debugging.

## Reference(s):

- [Fish Audio model overview](https://runapi.ai/models/fish-audio.md)
- [Fish Audio homepage](https://runapi.ai/models/fish-audio)
- [Fish Audio s1 variant](https://runapi.ai/models/fish-audio/s1.md)
- [Fish Audio s2-pro variant](https://runapi.ai/models/fish-audio/s2-pro.md)
- [Fish Audio s2.1-pro variant](https://runapi.ai/models/fish-audio/s2.1-pro.md)
- [Fish Audio provider page](https://runapi.ai/providers/fish-audio.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, SDK package names, request fields, and configuration notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include RunAPI CLI commands, SDK integration details, request JSON fields, and result-handling notes for RunAPI-managed audio URLs.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
