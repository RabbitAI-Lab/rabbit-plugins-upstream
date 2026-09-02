## Description:

Shapes agent behavior via instruction framing and style transfer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to frame agent prompts, skill instructions, multi-agent review dispatches, and style-matching generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt-framing guidance can reduce review quality if used outside the documented conditions, such as competitive framing for fewer than three reviewers or implementation agents.

Mitigation: Apply the module-specific when-not-to-use guidance and require evidence-backed findings when using competitive review framing.

Risk: Style transfer can reproduce outdated or inappropriate conventions if the exemplar is poorly chosen.

Mitigation: Use recent, high-quality exemplars from the same codebase and language, and keep exemplar snippets within the documented size guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-latent-space-engineering)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance for prompt and skill-authoring workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Markdown-only skill; it does not run commands or access private data.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
