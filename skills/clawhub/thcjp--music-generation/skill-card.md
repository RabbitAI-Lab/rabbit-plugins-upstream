## Description:

Generates AI music from prompts with style control and production-oriented audio output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, developers, and multimedia production teams use this skill to draft AI-generated music from prompts, select styles, and prepare audio outputs for creative projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command-execution authority without clear limits.

Mitigation: Install only in a constrained environment, review commands before execution, and require the publisher to narrow exec permissions and define exact file output behavior.

Risk: External music service calls and required credentials are not documented in the release evidence.

Mitigation: Require documentation of external services, credential requirements, and data handling before using the skill with sensitive prompts or production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/music-generation)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with optional JSON-shaped result examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce prompt guidance, style choices, file-handling instructions, and music-generation workflow steps.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
