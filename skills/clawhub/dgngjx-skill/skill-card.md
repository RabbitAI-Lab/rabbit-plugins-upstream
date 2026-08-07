## Description:

Dgngjx Skill is a multi-purpose utility toolbox for agents, covering image processing, PDF conversion, data conversion, text tools, developer tools, video tools, education, lifestyle utilities, practical utilities, and system tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for common utility work such as conversions, text analysis, file-oriented image/PDF/video tasks, HTTP checks, system checks, history lookup, and configuration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retain user activity, including input and output summaries, in a hidden local history file under ~/.workbuddy.

Mitigation: Review or disable history behavior before using confidential prompts, file paths, API endpoints, or work data, and clear ~/.workbuddy/dgngjx_history.json when needed.

Risk: Network-capable tools can contact third-party services or user-supplied URLs.

Mitigation: Review URLs before execution and avoid sending secrets, private endpoints, or sensitive work data through these tools.

Risk: The documentation gives an incorrect FAQ path for the history file.

Mitigation: Use the scanner-identified actual history path, ~/.workbuddy/dgngjx_history.json, when auditing or clearing stored history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/dgngjx-skill)
- [Source skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON snippets, and inline shell or Python commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some workflows may create or modify local files when the user chooses file-processing tools.]

## Skill Version(s):

3.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
