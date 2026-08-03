## Description: <br>
Use when someone wants an educational explainer with a host and characters - history or science shorts with dialogue, not voiceover-only B-roll. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, educators, and developers use this skill to plan and generate short educational videos that alternate host narration with expert or character dialogue. It guides intake, scene planning, still generation, TTS, video/avatar generation, review gates, and final assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can call paid or quota-consuming media-generation tools. <br>
Mitigation: Use the required approve plan, approve stills, and approve clips gates before allowing generation to continue. <br>
Risk: User-provided cast photos, locations, or reference plates may be uploaded to media-generation providers. <br>
Mitigation: Confirm that uploaded reference media is appropriate for provider processing and avoid sensitive media unless the user has approved that use. <br>
Risk: Generated educational videos can contain incorrect, misleading, or low-quality story beats. <br>
Mitigation: Review the scene table, stills, TTS timing, clips, and final assembly before delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/interactive-explainer) <br>
- [Educational explainer scenes](artifact/references/interactive-explainer-scenes.md) <br>
- [Educational explainer motion](artifact/references/interactive-explainer-motion.md) <br>
- [Interactive explainer prompts](artifact/references/interactive-explainer-prompts.md) <br>
- [Explainer plan template](artifact/templates/explainer-plan.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands] <br>
**Output Format:** [Markdown guidance with JSON plan structures, prompts, inline shell commands, and review gates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides production of image, audio, video, and assembled MP4 artifacts through dependent generation skills; includes approval gates before paid or quota-consuming generation.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
