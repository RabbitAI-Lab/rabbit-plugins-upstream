## Description: <br>
Guides agents to write diverse generative-media prompts with ritual seeds, explicit structure, scenario-axis rotation, and quality gates before paid generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and creative operators use this skill to plan image, video, and audio generation prompts, ask for missing creative or cost-sensitive details, rotate creative variables, and run quality or approval gates before paid generation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer agents toward external generative-media workflows that upload assets or spend credits. <br>
Mitigation: Keep approval gates enabled, clarify missing media and cost-sensitive choices, and get explicit user approval before paid generation phases. <br>
Risk: Generated images, video, or audio can contain quality, brand, legal, or safety issues that are easy to miss before later workflow steps. <br>
Mitigation: Open the real output files and run the relevant quality checklist before advancing to upscale, video, assembly, or final handoff. <br>
Risk: Voice, identity, gender, or visual examples in the guidance could be mistaken for user consent or required defaults. <br>
Mitigation: Confirm voice and identity choices explicitly and treat examples as illustrative rather than mandatory. <br>


## Reference(s): <br>
- [Clarification intake](references/clarification-intake.md) <br>
- [Generation diversity](references/generation-diversity.md) <br>
- [Generation quality checklist hub](references/generation-quality-checklists.md) <br>
- [Still-image prompt flow](references/still-image-prompt-flow.md) <br>
- [Workflow feedback gates](references/workflow-feedback-gates.md) <br>
- [String Seed of Thought](https://pub.sakana.ai/ssot/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with prompt templates, checklists, tables, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts, manifest notes, and approval gates are intended to be applied before paid media-generation calls.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
