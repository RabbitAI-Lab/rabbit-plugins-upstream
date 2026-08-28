## Description:

AI大模型专家｜短剧分集梗概 helps short-drama and manhua teams turn episode synopsis goals into executable outlines, story assets, generation prompts, validation criteria, and AI-HIVE image or video generation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creative, production, brand, ecommerce, ad-buying, and overseas distribution teams use this skill to plan short-drama episode synopses, decompose scripts into reusable character, story, scene, and shot assets, and prepare AI-HIVE generation commands for images and videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses remote AI-HIVE APIs and may upload user-selected media files.

Mitigation: Review files before upload and use only media the user is authorized to process.

Risk: The skill requires an AI-HIVE API key stored in AI_HIVE_API_KEY or ~/.ai-hive/config.json.

Mitigation: Protect the API key, keep the local config file private, and rotate or revoke keys if exposure is suspected.

Risk: Generated media may be downloaded locally when --no-download is not used.

Mitigation: Choose an appropriate output directory and inspect generated files before reuse or publication.

Risk: Short-drama planning and generated content can include inaccurate brand, product, identity, or rights claims.

Mitigation: Require user-confirmed facts and rights checks before publishing scripts, prompts, images, or videos.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-episode-synopsis)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local planning JSON files, upload user-selected media, poll remote AI-HIVE tasks, and download generated image or video files when downloads are enabled.]

## Skill Version(s):

1.0.0 (source: server release and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
