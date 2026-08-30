## Description:

This skill helps brands, MCNs, virtual-IP studios, and content creators turn AI virtual influencer or digital-IP requests into character positioning, story and visual planning, production commands, generated image or video tasks, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, MCN, virtual-IP, and content-production users use this skill to define virtual influencer concepts, plan reusable character assets, generate scripts and production task lists, and optionally run AI-HIVE image or video generation workflows. Developers can also use the included Python helpers to create briefs, upload authorized media, query AI-HIVE model and pricing data, submit asynchronous generation tasks, download results, and perform deterministic local video edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE image or video generation may incur cost or upload user-provided media.

Mitigation: Review generated commands and final parameters before execution, confirm pricing before generation, and use only media the user is authorized to upload.

Risk: The workflow relies on an AI-HIVE API key stored in the environment or local configuration.

Mitigation: Keep the API key out of prompts, logs, screenshots, and version control, and use local configuration permissions that limit other users' access.

Risk: Generated influencer content can misstate facts, imply unauthorized endorsements, or resemble protected people, brands, or IP.

Mitigation: Verify factual claims, disclose AI or sponsorship status when required, confirm rights to references, and reject requests to impersonate real people or existing IP without authorization.

Risk: Local video helper commands can overwrite output files when ffmpeg is invoked with replacement flags.

Mitigation: Review paths before running commands, keep source media unchanged, and write generated edits to distinct output locations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-virtual-influencer-incubator-ai-hive)
- [AI-HIVE application](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON briefs, Python helper commands, shell examples, task records, and review checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE API calls, media upload steps, asynchronous task IDs, pricing snapshots, downloaded file paths, and local ffmpeg processing commands.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
