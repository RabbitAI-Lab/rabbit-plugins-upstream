## Description: <br>
Use when someone wants an educational explainer with a host and characters, such as history or science shorts with dialogue rather than voiceover-only B-roll. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, educators, and developers use this skill to plan educational short videos that alternate host narration with on-camera expert or character dialogue. It supports history, science, nature, how-it-works, and children's explainer workflows with staged review gates before generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on prerequisite Pruna media-generation skills that may make paid API calls. <br>
Mitigation: Confirm the prerequisite skills, expected API usage, and approval gates before generating stills, audio, video, or music. <br>
Risk: The artifact uses binary persona gender and voice-matching fields for avatar scenes. <br>
Mitigation: Review cast and voice requirements before use, and adapt the plan manually when nonbinary, unspecified, or user-selected voice handling is needed. <br>
Risk: Generated educational videos can become misleading if the scene plan lacks factual depth or causal structure. <br>
Mitigation: Review the scene table and stand-alone test at the plan gate before approving media generation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/pruna-ai/skills/interactive-explainer) <br>
- [Educational Explainer Scenes](artifact/references/interactive-explainer-scenes.md) <br>
- [Educational Explainer Motion](artifact/references/interactive-explainer-motion.md) <br>
- [Interactive Explainer Prompts](artifact/references/interactive-explainer-prompts.md) <br>
- [Explainer Plan Template](artifact/templates/explainer-plan.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON plan structure and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides staged media generation with user approval gates before paid calls.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
