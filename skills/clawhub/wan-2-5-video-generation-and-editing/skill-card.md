## Description:

Wan2.5 Video Generation and Editing helps video editors, post-production teams, advertisers, e-commerce operators, and creators generate or edit deliverable videos from text prompts and optional image, video, or audio references through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video production teams, e-commerce sellers, and marketing operators use this skill to submit Wan2.5 text-to-video, image-to-video, reference-to-video, video-editing, and audio-conditioned video generation jobs. The skill uploads selected media, submits AI Hive generation tasks, tracks task status, and can download generated video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected media may be uploaded to AI Hive during generation or upload flows.

Mitigation: Review media contents before use and avoid submitting sensitive, private, or restricted files unless the AI Hive handling terms are acceptable.

Risk: Video generation can incur API costs, especially for repeated or bulk jobs.

Mitigation: Check runtime pricing, use the default cost-first routing where appropriate, and use --no-download for submit-only runs when task submission and later review are sufficient.

Risk: The init flow stores an AI Hive API key on the local machine.

Mitigation: Keep the local configuration file private, prefer environment variables where operationally appropriate, and rotate the API key if it may have been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/wan-2-5-video-generation-and-editing)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API key console](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The associated script can submit AI Hive video jobs, return task identifiers, and download generated media files when download is enabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
