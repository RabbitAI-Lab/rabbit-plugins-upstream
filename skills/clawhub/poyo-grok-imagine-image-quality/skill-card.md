## Description: <br>
Grok Imagine Image Quality generation and editing on PoYo / poyo.ai via https://api.poyo.ai/api/generate/submit for text-to-image, reference-image editing, aspect ratio, 1K or 2K output, output format, async polling, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare and optionally submit PoYo Grok Imagine Image Quality text-to-image or reference-image editing jobs. It helps form request payloads, choose supported image parameters, and explain task polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY could be exposed if placed in client code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep the key server-side in an environment variable or secret manager and send it only in the PoYo Authorization header. <br>
Risk: Prompts, reference image URLs, callback URLs, or generated result URLs may contain sensitive information shared with PoYo or a webhook receiver. <br>
Mitigation: Avoid confidential prompts, private image URLs, and sensitive callback URLs unless the user trusts PoYo and the webhook receiver. <br>
Risk: A live submission sends network traffic to the PoYo generation endpoint and may start billable or externally processed work. <br>
Mitigation: Submit only after the user explicitly requests a live call and reviews the JSON payload in a safe server-side environment. <br>
Risk: PoYo field support and service behavior may change over time. <br>
Mitigation: Verify current PoYo documentation before production use, especially for output count, sync behavior, status states, and accepted image parameters. <br>


## Reference(s): <br>
- [PoYo Grok Imagine Image Quality model page](https://poyo.ai/models/grok-imagine-image-quality) <br>
- [PoYo Grok Imagine Image Quality API docs](https://docs.poyo.ai/api-manual/image-series/grok-imagine-image-quality) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [Local API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-grok-imagine-image-quality) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id after an explicitly requested live submission; requires POYO_API_KEY for API calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
