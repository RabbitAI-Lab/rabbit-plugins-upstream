## Description:

Transforms vague prompts into precise, structured AI instructions for prompt refinement, prompt engineering, and system prompt writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to turn vague prompt requests into precise, structured AI instructions. It is suited for refining prompts, writing system prompts, and validating that a prompt states task, constraints, context, and output format clearly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can offer to save refined prompts locally, which could persist sensitive or incorrect instructions if approved without review.

Mitigation: Require explicit user confirmation before writing and review the refined prompt before saving.

Risk: Prompt refinement can accidentally change user intent by adding unsupported constraints.

Mitigation: Use only information present in the original prompt or conversation context and ask for clarification when critical information is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-refine-prompt)
- [Skill specification](artifact/SPEC.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown refined prompt, with an optional confirmation step before saving locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Refined output targets 0.75x-1.5x the original prompt unless structural changes justify otherwise; local persistence requires user confirmation.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
