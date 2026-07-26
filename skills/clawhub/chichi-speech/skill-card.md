## Description: <br>
A RESTful service for high-quality text-to-speech using Qwen3 and specialized voice cloning. Optimized for reusing a specific voice prompt to avoid re-computation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hudeven](https://clawhub.ai/user/hudeven) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to install and run a local FastAPI text-to-speech service that synthesizes WAV audio from text with a reusable Qwen3 voice-cloning reference prompt. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The service may be reachable by other machines if bound to a non-localhost interface. <br>
Mitigation: Run with --host 127.0.0.1 for local use and add appropriate access controls before exposing it on a network. <br>
Risk: Voice cloning can misuse a speaker's likeness or create misleading speech. <br>
Mitigation: Use only reference audio from speakers who have explicitly consented, and do not use generated speech for impersonation, fraud, or deception. <br>
Risk: Large external ML model downloads and unpinned dependencies can create operational and supply-chain exposure. <br>
Mitigation: Install in an isolated Python environment, pin and update dependencies, and review model download behavior before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hudeven/skills/chichi-speech) <br>
- [Qwen3 sample reference audio](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/clone_2.wav) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, Files] <br>
**Output Format:** [Markdown with shell commands, JSON request examples, and WAV audio output from the service] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The service exposes a /synthesize endpoint and can stream or save audio/wav output.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
