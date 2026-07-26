## Description: <br>
Generate high-quality English speech offline on CPU using 8 built-in voices or custom voice cloning with Kyutai's Pocket TTS model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sherajdev](https://clawhub.ai/user/sherajdev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to install and operate a local text-to-speech workflow that converts English text into speech, selects built-in voices, or uses a WAV prompt for voice cloning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First use may require downloading Python dependencies and model files, and Hugging Face model access may be gated by license acceptance. <br>
Mitigation: Confirm the deployment environment permits dependency and model downloads, accept the model license before use, and prefetch or cache approved artifacts where needed. <br>
Risk: Voice cloning can misuse a speaker's voice or expose sensitive voice samples. <br>
Mitigation: Use voice cloning only with clear speaker consent, keep voice samples protected as sensitive personal data, and review generated audio before distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sherajdev/skills/pocket-tts) <br>
- [Kyutai Pocket TTS demo](https://kyutai.org/tts) <br>
- [Kyutai Pocket TTS Hugging Face model](https://huggingface.co/kyutai/pocket-tts) <br>
- [Kyutai Pocket TTS paper](https://arxiv.org/abs/2509.06926) <br>
- [Kyutai Pocket TTS GitHub repository](https://github.com/kyutai-labs/pocket-tts) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Files] <br>
**Output Format:** [Markdown guidance with inline bash and Python examples; runtime output is WAV audio.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may download model assets on first use and can generate speech from built-in voices or a user-provided WAV prompt.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
