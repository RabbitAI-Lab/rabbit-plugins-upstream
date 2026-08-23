## Description:

Turns product facts, feature notes, and existing media into structured product-explainer video plans and AI Hive generation commands for 15-second, 30-second, tutorial, FAQ, edit, and extension workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and developers use this skill to convert approved product information, product media, and support scenarios into concise explainer-video scripts, shot structure, and AI Hive video-generation commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and media may be sent to AI Hive during generation.

Mitigation: Use only product media and approved claims that are acceptable to process through AI Hive, and review the AI Hive account and API-key terms before use.

Risk: A persistent API key file can expose account access if the local machine or user profile is not protected.

Mitigation: Protect ~/.ai-hive/config.json and prefer the AI_HIVE_API_KEY environment variable when a persistent key file is not desired.

Risk: Generated product videos can misstate features, parameters, certifications, pricing, or effects if source facts are incomplete.

Mitigation: Review generated scripts and media against approved product facts, supplied materials, and platform policy before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-explainer-video-generation)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with bash command examples; CLI task responses may be JSON and generated media may be downloaded as local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key, accepts prompt text and optional product media, can upload media for generation, and can download generated video or image outputs to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
