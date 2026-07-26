## Description: <br>
FLUX Schnell text-to-image generation on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use when the user explicitly requests PoYo or `flux-schnell` for prompt-based image generation, output size, image count, PNG or JPEG output, async polling, or webhooks; do not use for image editing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare reviewed PoYo FLUX Schnell text-to-image payloads, submit approved asynchronous generation jobs, and explain polling or webhook follow-up. It is for prompt-based image generation only, not image editing or image-to-image workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, callback URLs, and generated image results are submitted to PoYo during live API use. <br>
Mitigation: Confirm the user trusts PoYo before submission and avoid confidential prompts, private callback URLs, and sensitive result URLs. <br>
Risk: POYO_API_KEY can be exposed if copied into client code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Keep the key server-side in the POYO_API_KEY environment variable or a secret manager and send it only in the PoYo Authorization header. <br>
Risk: A live submission contacts PoYo and may create provider-side usage or billing. <br>
Mitigation: Require explicit user approval for live calls and review the payload JSON before running the helper. <br>


## Reference(s): <br>
- [PoYo FLUX Schnell API Reference](references/api.md) <br>
- [PoYo FLUX Schnell model page](https://poyo.ai/models/flux-schnell) <br>
- [PoYo FLUX Schnell API docs](https://docs.poyo.ai/api-manual/image-series/flux-schnell) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-flux-schnell) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/coolhackboy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id after an explicitly approved live submission.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
