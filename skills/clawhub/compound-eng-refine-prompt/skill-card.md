## Description:

Transforms vague prompts into precise, structured AI instructions for prompt refinement, prompt engineering, system prompts, and agent instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, prompt engineers, and agent builders use this skill to turn vague prompt drafts into precise, structured instructions and to validate that the refined prompt preserves the original intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A refined prompt could unintentionally change the user's original intent or introduce unsupported constraints.

Mitigation: Review the refined prompt before use and verify it only uses information from the original prompt or conversation context.

Risk: Optional persistence could write prompt content to a local file.

Mitigation: Save refined prompts only after explicit user approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-refine-prompt)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown refined prompt text, with optional saved Markdown after explicit user approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks for clarification when intent is unclear and declines harmful or illegal prompt-refinement requests.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
