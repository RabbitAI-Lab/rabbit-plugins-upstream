## Description: <br>
Two-layer content safety for agent input and output, including prompt injection detection for input and optional content moderation for input and output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zskyx](https://clawhub.ai/user/zskyx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to screen untrusted user messages and draft agent output before an agent acts or responds in public-facing or multi-user environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Moderated input, and optionally draft output, is sent to Hugging Face and OpenAI APIs. <br>
Mitigation: Use scoped API keys and avoid sending secrets or regulated data unless approved for those services. <br>
Risk: A failed or unavailable API check can leave the moderation signal incomplete. <br>
Mitigation: Treat unavailable checks as missing signal rather than proof that content is safe, and fall back to human or agent policy review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zskyx/skills/detect-injection) <br>
- [Hugging Face Inference API endpoint used by the helper script](https://router.huggingface.co/hf-inference/models/$MODEL) <br>
- [OpenAI moderations API endpoint used by the helper script](https://api.openai.com/v1/moderations) <br>


## Skill Output: <br>
**Output Type(s):** [json, shell commands, guidance] <br>
**Output Format:** [JSON verdicts with optional action guidance and shell command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HF_TOKEN for prompt injection detection; OPENAI_API_KEY optionally enables content moderation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
