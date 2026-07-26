## Description: <br>
Create a custom voice and speak text in it by cloning from an audio sample or designing a new voice from a written description. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to collect voice-cloning or voice-design inputs, choose an appropriate audio model, and guide generation of consistent custom speech while respecting likeness consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reference voice audio may contain sensitive likeness data and is uploaded to the configured model provider. <br>
Mitigation: Use the skill only when the user owns the voice or has explicit permission, and confirm comfort with uploading reference audio before generation. <br>
Risk: Voice cloning can be misused to imitate a third party without permission. <br>
Mitigation: Refuse requests to clone a third party's voice unless explicit rights or consent are confirmed. <br>
Risk: Noisy, multi-speaker, or low-quality reference recordings can reduce clone similarity and output quality. <br>
Mitigation: Ask for a clean, dry, single-speaker sample and review generated audio for clipping, garble, drift, or unintended tail audio. <br>


## Reference(s): <br>
- [ClawHub Voice Cloning skill page](https://clawhub.ai/runware/skills/voice-cloning) <br>
- [Runware publisher profile](https://clawhub.ai/user/runware) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with model identifiers, request parameters, and operational checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides asynchronous audio generation, reference-audio handling, consent checks, and quality review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
