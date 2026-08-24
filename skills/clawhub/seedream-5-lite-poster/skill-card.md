## Description:

Seedream 5.0 Lite 海报生成 helps agents create poster-generation prompts and run a fixed AI Hive Seedream 5.0 Lite image workflow with distance-based layout checks for focus, hierarchy, and detail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and designers use this skill to draft poster concepts and generate approved visual backgrounds for events, courses, product launches, social posts, and marketing materials. Developers or agents can run the included AI Hive helper to submit generation jobs, upload approved reference images, query tasks, and save outputs locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key for generation requests.

Mitigation: Use a dedicated key with approved access, store it through the documented environment variable or local config path, and rotate it if exposed.

Risk: Optional reference images are uploaded to AI Hive and object storage during generation.

Mitigation: Upload only approved, non-sensitive images that the user has rights to use.

Risk: Generated poster backgrounds may include incorrect text, dates, prices, brands, or other unsupported details.

Mitigation: Use the skill's distance checks and final human review; add approved copy, dates, prices, logos, and QR codes in a design tool after generation.

Risk: Generated outputs are saved to a local directory.

Mitigation: Choose an appropriate output directory and handle saved images according to the user's data-handling policy.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/seedream-5-lite-poster)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and locally saved generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key, supports optional approved reference-image uploads, polls generation tasks, and downloads successful image outputs to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
