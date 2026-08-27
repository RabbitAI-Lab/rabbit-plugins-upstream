## Description:

Helps Seedream 5 image creators, brand designers, and ecommerce visual teams turn image-generation requests into Chinese production workflows, prompts, reference-image plans, batch variants, runnable AI-HIVE commands, and quality checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand designers, ecommerce teams, and developers use this skill to plan, generate, track, and evaluate Seedream 5 image assets through AI-HIVE. It emphasizes authorized source material, review before paid generation, routing choices, task records, and platform-ready deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation commands can incur AI-HIVE costs and may upload user-provided media.

Mitigation: Confirm the prompt, uploaded files, routing mode, batch size, and expected cost before running generation commands.

Risk: The skill can store an AI-HIVE API key in ~/.ai-hive/config.json.

Mitigation: Treat the config file as a local secret store and remove or rotate the key on shared machines or when the key is no longer needed.

Risk: Generated commercial imagery can contain inaccurate claims or unauthorized references if inputs are not reviewed.

Mitigation: Use only authorized source material and review product facts, brand claims, likenesses, platform rules, and generated outputs before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/seedream-5-image-studio-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local blueprint JSON files, upload user-provided media to AI-HIVE, submit asynchronous generation tasks, and download generated image or video files when the user confirms paid execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
