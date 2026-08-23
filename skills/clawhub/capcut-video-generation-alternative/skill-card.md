## Description:

Generates slot-specific AI Hive Seedance 2.5 video clips for Jianying, CapCut, and short-form editing timelines, including B-roll, openers, matched shots, clean plates, and tail extensions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and developers use this skill to plan and generate short video inserts that can be added back into Jianying, CapCut, or another nonlinear editor. It helps fill timeline gaps with approved media-aware prompts and generated clip outputs rather than replacing a full editing workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected images or videos to AI Hive for generation.

Mitigation: Use only media the user is authorized to upload, and confirm the user trusts AI Hive before running insert or ingest commands.

Risk: The CLI stores an AI Hive API key under the user's home directory.

Mitigation: Prefer environment-provided credentials when appropriate, restrict the stored key file to owner-only permissions, and rotate the key if it is exposed.

Risk: Generated clips may contain unsuitable, inaccurate, or rights-sensitive content before they are placed into an editing timeline.

Mitigation: Review downloaded results for visual quality, rights, brand safety, and timeline fit before adding them to Jianying, CapCut, or another editor.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/capcut-video-generation-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and CLI-generated JSON or status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-selected images or videos to AI Hive and may download generated MP4 clips to the user's Downloads/AiHive directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
