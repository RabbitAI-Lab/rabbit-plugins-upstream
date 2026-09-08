## Description:

Use when writing any generative prompt - ritual seed, explicit structure, scenario axes, and quality gates before paid API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to draft diverse prompts for image, video, and audio generation, preserve user-provided creative locks, and run quality gates before paid generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned install examples can resolve to newer package contents than the reviewed release.

Mitigation: Install only from trusted sources and review the resolved skill version before use.

Risk: Skipping approval gates can spend paid generation credits or advance weak assets into later workflow stages.

Mitigation: Keep plan, stills, clips, and final assembly gates enabled unless the user explicitly opts into automation.

Risk: Remote media workflows may upload user assets to external services.

Mitigation: Confirm with the user before uploading assets and preserve any user-provided privacy or usage constraints.

Risk: Example identity categories may not match a real person's stated or unknown identity.

Mitigation: Treat examples as prompt structure only and follow the user's supplied identity information when present.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/generation-diversity)
- [Clarification intake](references/clarification-intake.md)
- [Generation diversity](references/generation-diversity.md)
- [Generation quality checklist hub](references/generation-quality-checklists.md)
- [Still-image prompt flow](references/still-image-prompt-flow.md)
- [Workflow feedback gates](references/workflow-feedback-gates.md)
- [String Seed of Thought](https://pub.sakana.ai/ssot/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with checklists, prompt structures, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval gates before paid generation and quality checks before downstream media steps.]

## Skill Version(s):

1.0.11 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
