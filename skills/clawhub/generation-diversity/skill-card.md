## Description:

Use when writing any generative prompt - ritual seed, explicit structure, scenario axes, and quality gates before paid API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and content-production agents use this skill to draft diverse image, video, and audio generation prompts, clarify missing creative requirements, and run quality gates before spending on generation calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad activation language for generative prompting and could influence workflows where generation diversity or QA guidance was not intended.

Mitigation: Use it only when the task calls for generation diversity, prompt structure, clarification intake, or generation quality review.

Risk: Install examples can add this skill or a related skill suite, which may expand the agent's active guidance set.

Mitigation: Prefer trusted, version-pinned installation paths and review the related skills before adding the full suite.

Risk: Skipping approval gates before paid image, video, or audio generation can waste credits or advance low-quality assets.

Mitigation: Follow the documented clarification, plan, stills, clip, and quality-check gates before paid generation steps.

## Reference(s):

- [Clarification intake](references/clarification-intake.md)
- [Generation diversity](references/generation-diversity.md)
- [Generation quality checklist hub](references/generation-quality-checklists.md)
- [Still-image prompt flow](references/still-image-prompt-flow.md)
- [Workflow feedback gates](references/workflow-feedback-gates.md)
- [String Seed of Thought](https://pub.sakana.ai/ssot/)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/generation-diversity)
- [ClawHub publisher profile](https://clawhub.ai/user/pruna-ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with checklists, prompt templates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces planning and review guidance for generation workflows; ritual seed strings are planning aids and should not be passed as API seeds unless the user explicitly asks for reproducibility.]

## Skill Version(s):

1.0.13 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
