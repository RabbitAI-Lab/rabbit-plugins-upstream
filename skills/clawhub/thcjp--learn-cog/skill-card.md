## Description:

AI-powered personalized learning assistant for project tutorials, language practice, writing feedback, visual learning, study guides, concept explanations, and homework support across STEM, humanities, technical, and career skill domains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Students, developers, and lifelong learners use this skill to request personalized explanations, learning plans, practice materials, writing feedback, language exercises, and project-based tutorials through natural-language prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command-execution authority without narrow boundaries.

Mitigation: Enable it only in workspaces where file access and shell execution are acceptable, explicitly user-directed, and reviewed before execution.

Risk: The skill may require API keys, SDK installation, and callback URLs.

Mitigation: Use environment variables for credentials, avoid committing secrets, and approve external callbacks only when the destination is trusted.

Risk: Generated educational, medical, legal, or other specialized content may be incomplete or inaccurate.

Mitigation: Review high-impact outputs with a qualified human or authoritative source before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/learn-cog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or structured JSON with examples, code snippets, study materials, and troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include executable setup commands, environment-variable guidance, generated learning content, and callback-oriented workflow descriptions.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
