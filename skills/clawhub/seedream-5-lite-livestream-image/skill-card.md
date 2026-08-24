## Description:

使用 Seedream 5.0 Lite 按直播时间轴制作预告、开场、讲解、机制、转场和回放图片，并设置有效期与实时信息占位。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, designers, and commerce teams use this skill to generate Seedream 5.0 Lite livestream commerce images organized by run-of-show timing, including teaser, opening, product explanation, promotion mechanism, transition, ending, and replay assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper may save an AI Hive API key under ~/.ai-hive/config.json on the local machine.

Mitigation: Use environment or command-line credentials where appropriate, keep the config file private, and remove or rotate the key on shared machines.

Risk: Reference images supplied by the user may be uploaded to AI Hive or object storage for generation tasks.

Mitigation: Use only approved images and prompts, and avoid uploading confidential, unauthorized, or unlicensed assets.

Risk: Livestream prices, inventory, discounts, countdowns, disclosures, and platform rules can change quickly.

Mitigation: Keep real-time commercial fields as placeholders until final approval, review disclosures before broadcast, and retire expired assets promptly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-livestream-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and generated image files saved by the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the fixed public_model_seedream_5_0_lite image model through AI Hive; accepts optional approved reference images and model parameters such as aspect_ratio.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
