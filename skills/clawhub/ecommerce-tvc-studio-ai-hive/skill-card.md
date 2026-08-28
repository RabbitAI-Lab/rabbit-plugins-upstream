## Description:

Turns e-commerce TVC and commercial video requests into a Chinese production workflow with creative concepts, storyboards, prompts, AI-HIVE generation steps, task records, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand marketers, e-commerce campaign teams, and advertising production teams use this skill to convert product goals, authorized media, channel constraints, duration, and budget into reviewable TVC production plans and runnable AI-HIVE media-generation commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation commands may create billable work.

Mitigation: Review the final prompt, model, routing mode, and expected cost before running generation commands; use small samples before batch tasks.

Risk: Uploaded reference media may contain content the user is not authorized to use.

Mitigation: Upload only media with confirmed usage rights and keep unlicensed references to abstract structure guidance rather than direct reuse.

Risk: API keys could be exposed in logs, screenshots, or shared files.

Mitigation: Use environment variables or the local config flow, avoid pasting real keys into prompts, and remove credentials from logs before sharing.

Risk: Advertising output may include unsupported product claims, fake testimonials, or misleading performance promises.

Mitigation: Require source-backed facts for claims and avoid guarantees about traffic, sales, rankings, approval, or return on investment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-tvc-studio-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with bash command examples, JSON task records, and optional generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a local production-brief JSON file and downloaded image or video files when the helper scripts are run.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
