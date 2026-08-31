## Description:

Helps 3C product, digital commerce, technology media, and product training teams turn real product images, official specifications, structural materials, feature steps, platform requirements, and duration targets into feature-explanation scripts, structural keyframes, usage-scene videos, parameter cards, AI-HIVE generation commands, and acceptance checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, 3C brands, digital commerce teams, technology media, and product training teams use this skill to plan and generate Chinese product-structure and feature-explanation video workflows. It emphasizes reviewable briefs, factual anchors from official product data, authorized media inputs, AI-HIVE model routing, task tracking, and platform-specific acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an AI-HIVE API key and may submit paid image or video generation tasks.

Mitigation: Treat the API key as sensitive, review prompts, selected mode, routing, model configuration, and price snapshot before submission, and run a small sample before batch generation.

Risk: Uploaded images, videos, audio, logos, product data, and reference media may be unauthorized or sensitive.

Mitigation: Upload only media the user is authorized to use and keep unverified reference material to abstract structure advice rather than close reproduction.

Risk: Generated product visuals or claims could misrepresent engineering structure, safety tests, specifications, pricing, performance, or market outcomes.

Mitigation: Anchor claims in official product materials, mark uncertain facts for verification, and do not present generated visuals as real engineering evidence or guaranteed commercial performance.

Risk: Local video processing uses ffmpeg on user-supplied files and can overwrite requested output paths.

Mitigation: Keep original files, inspect input and output paths before running edit commands, and use deterministic probe, trim, aspect, mute, loudnorm, or concat operations only on intended media.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/electronics-feature-explainer-ai-hive)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON task records, and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local blueprint JSON files, upload authorized media to AI-HIVE, poll asynchronous generation tasks, download generated images or videos, and run deterministic ffmpeg edits when invoked by the user.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
