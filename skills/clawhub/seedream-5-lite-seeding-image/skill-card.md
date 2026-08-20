## Description:

使用 Seedream 5.0 Lite 为推荐笔记建立可见事实、作者判断与需证明说法的分层画面，并预留合作关系和 AI 合成披露。Use this skill for Seedream 5 Lite recommendation visuals、种草图片、小红书笔记、抖音好物内容、Instagram UGC、创作者合作图、开箱观察、使用记录、生活方式内容和透明商业传播；通过 AI Hive 处理授权素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and agents use this skill to generate Seedream 5.0 Lite recommendation visuals from authorized product materials while separating visible facts, creator judgments, and brand-substantiated claims. It supports social commerce and UGC workflows that need explicit collaboration and AI-synthesis disclosure areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any named reference images are sent to AI Hive for generation.

Mitigation: Use only images and product materials you are authorized to upload, and avoid including sensitive or private content in prompts or reference files.

Risk: The init flow can store an AI Hive API key on the local machine.

Mitigation: Prefer scoped credentials, keep the local config file private, and rotate the key if it is exposed.

Risk: Generated recommendation visuals may imply unsupported marketing claims or endorsements if reviewed poorly.

Mitigation: Maintain the claim register described by the skill, require human review for creator judgments and brand claims, and keep collaboration and AI-synthesis disclosures visible before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-seeding-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands; generated tasks return JSON status and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses fixed Seedream 5.0 Lite model public_model_seedream_5_0_lite; supports optional authorized image uploads, routing mode, batch size, key=value model parameters, task polling, and local output directory selection.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
