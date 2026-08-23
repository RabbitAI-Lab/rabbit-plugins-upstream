## Description:

This skill helps users migrate Chinese image generation and reference-image editing workflows from Jimeng or Dreamina-style prompts to AI Hive Nano Banana Pro while preserving prompt intent, reference-image roles, subject continuity, and commercial delivery requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, designers, and developers use this skill to convert Dreamina or Jimeng-style Chinese image prompts and reference-image editing tasks into AI Hive image generation commands. It supports commercial image drafts, product scenes, character continuity, multi-reference composition, task lookup, and local result download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected reference images are sent to AI Hive for generation.

Mitigation: Use the skill only with prompts and reference images that are appropriate to share with AI Hive.

Risk: An AI Hive API key may be stored locally or supplied through an environment variable.

Mitigation: Store the key with restricted file permissions or use AI_HIVE_API_KEY, and rotate the key if it is exposed.

Risk: Broad trigger wording may activate the skill for general replacement or migration requests.

Mitigation: Review the trigger wording before installation if activation should be limited to specific Dreamina or Jimeng migration tasks.

## Reference(s):

- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/dreamina-image-generation-editing-alternative)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands; CLI output includes task JSON and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally unless no-download mode is used; selected reference images and prompts are sent to AI Hive.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
