## Description:

This skill turns avatar try-on video requests into production plans, prompts, runnable AI-HIVE commands, task records, and quality checks for fashion ecommerce and marketing teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion ecommerce, advertising, social commerce, and content teams use this skill to plan and optionally generate short avatar try-on videos from authorized garment and person references. It helps produce reviewable storyboards, prompt sets, AI-HIVE task commands, task tracking details, and acceptance checks before paid generation work proceeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide media they do not have rights to use.

Mitigation: Use only authorized garment, person, brand, logo, audio, video, and reference materials; if rights are unclear, provide abstract planning guidance rather than generated imitation.

Risk: Selected local media may be uploaded to AI-HIVE and generated outputs may be saved locally.

Mitigation: Confirm upload scope before generation, avoid sensitive or unauthorized files, and store downloaded outputs only in approved local locations.

Risk: Generation tasks may incur costs or use an unintended model route.

Mitigation: Review the prompt, model, routing mode, and pricing snapshot before submitting tasks; use small samples before batch work.

Risk: API keys can be exposed if copied into logs, files, screenshots, or shared machines.

Mitigation: Use placeholders in examples, prefer environment variables or trusted local configuration, and keep any stored API-key file restricted to the current user.

Risk: Avatar try-on videos can be mistaken for proof of real fit, material behavior, endorsement, or product performance.

Mitigation: Label the output as a marketing visual preview, verify product claims against real sources, and do not present generated people or brands as authentic endorsements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/avatar-try-on-video-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands, JSON task records, prompts, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local JSON briefs and command lines that upload authorized media to AI-HIVE, submit generation tasks, poll task status, and download generated media when executed with user-provided credentials.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
