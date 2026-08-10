## Description: <br>
Use when someone wants an educational explainer with a host and characters for history or science shorts with dialogue, not voiceover-only B-roll. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to plan and run educational short-form explainers that alternate host narration with expert or character dialogue. It guides intake, scene planning, still generation, TTS, video generation, review gates, and final assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can spend generation credits through image, TTS, video, avatar, and audio generation steps. <br>
Mitigation: Use the documented approval gates before paid calls: approve plan, approve stills, and approve clips. <br>
Risk: User-provided cast photos, location images, or reference media may be uploaded to generation providers. <br>
Mitigation: Confirm the media source and user approval before using uploaded reference assets in generation steps. <br>
Risk: Generated educational explainers can become misleading if the scene plan lacks factual grounding or review. <br>
Mitigation: Review the full scene table, dialogue arc, and final clips before assembly and delivery. <br>
Risk: The avatar workflow currently assumes binary persona gender and voice categories. <br>
Mitigation: Override or avoid those cast fields when they do not fit the subject or intended representation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/interactive-explainer) <br>
- [Educational explainer scenes](references/interactive-explainer-scenes.md) <br>
- [Educational explainer motion](references/interactive-explainer-motion.md) <br>
- [Interactive explainer prompts](references/interactive-explainer-prompts.md) <br>
- [Explainer plan template](templates/explainer-plan.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON plan files and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide approved generation of still images, TTS audio, video clips, and assembled MP4 deliverables.] <br>

## Skill Version(s): <br>
1.0.9 (source: artifact frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
