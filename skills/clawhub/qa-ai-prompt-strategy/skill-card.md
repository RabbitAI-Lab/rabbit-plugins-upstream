## Description:

Selects structured prompt patterns for AI-assisted QA test-case generation so an agent can produce optimized prompts with role definitions, output formats, and constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and testing teams use this skill to choose prompt strategies when AI-generated test cases are too generic or shallow. It helps an agent turn a supplied QA context package into a stronger prompt for generating executable and verifiable test cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be invoked in broad prompt-improvement conversations because its trigger language covers general prompt optimization terms.

Mitigation: Scope use to QA testing workflows and supplied context packages, as recommended by the security guidance.

Risk: Prompt templates may produce plausible but incomplete testing guidance if the supplied QA context is sparse or inaccurate.

Mitigation: Review generated prompts and test cases against the source requirements, and use the skill's critique or adversarial patterns to check assumptions and coverage gaps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-ai-prompt-strategy)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown prompt templates and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces optimized prompts, role definitions, output format specifications, and constraint lists; it does not produce unique traceability IDs.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
