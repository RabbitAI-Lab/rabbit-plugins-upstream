## Description: <br>
Voice Builder helps an agent analyze real writing samples and produce a reusable voice.md guide for writing in a person or brand's voice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and content teams use this skill to capture a person or brand's writing patterns from real samples, then produce an operational voice.md guide that downstream writing skills can follow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Writing samples, transcripts, or private conversations can contain personal, customer, or confidential business information. <br>
Mitigation: Use samples the user created or is authorized to share, obtain consent for recordings or private conversations when applicable, and redact names, contact details, customer data, and confidential business information before generating voice.md. <br>
Risk: A voice guide built from thin, inconsistent, ghostwritten, or AI-generated samples can misrepresent the person or brand. <br>
Mitigation: Require real representative samples, mark low-confidence guides when evidence is thin, exclude unsuitable samples, and validate the guide with a generated test post scored against the voice fingerprint. <br>


## Reference(s): <br>
- [Voice Builder Skill Page](https://clawhub.ai/social-media-skills/skills/voice-builder) <br>
- [Samples Guide](references/samples-guide.md) <br>
- [Voice Analysis Framework](references/analysis-framework.md) <br>
- [Voice Template](references/voice-template.md) <br>
- [Validation Guide](references/validation.md) <br>
- [Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance and a voice.md file structure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided writing samples, cites evidence, and includes validation scoring before finalizing the guide.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
