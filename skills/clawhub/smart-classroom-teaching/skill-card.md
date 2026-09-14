## Description:

Smart Classroom Teaching helps an agent plan, analyze, and present classroom instruction through teaching visualization, Socratic dialogue, classroom-record analysis, personalized tutoring, multimodal command handling, teaching-resource generation, and education safety checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, students, and education developers use this skill to turn natural-language classroom requests into lesson plans, teaching scripts, diagnostic reports, visual explanations, personalized tutoring flows, and workbench state for classroom presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student or classroom state may include identifiable or sensitive education data.

Mitigation: Use anonymized or synthetic classroom data, apply the skill's privacy-redaction step before rendering, and delete exported history or state files when they are no longer needed.

Risk: The optional localhost state service is unauthenticated and uses permissive CORS.

Mitigation: Run the service only for trusted local sessions, stop it immediately after use, avoid browsing untrusted sites while it is active, and add per-session authorization and stricter CORS before shared deployment.

Risk: Workbench rendering of untrusted lesson JSON, HTML, or SVG can expose users to unsafe content.

Mitigation: Load only trusted state sources, review generated visual code before display, and add schema validation plus sanitization before production classroom use.

Risk: Large or malformed state payloads can degrade the local workbench experience.

Mitigation: Validate the state schema and enforce practical request-size limits before accepting external updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/smart-classroom-teaching)
- [Smart classroom task catalog](references/smart-classroom-catalog.md)
- [Smart classroom task requirements](references/smart-classroom-requirements.md)
- [Smart classroom exemplars index](references/smart-classroom-exemplars.md)
- [Smart classroom workbench](assets/smart-classroom-workbench.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON classroom state, optional SVG/HTML/code snippets, and local shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use an optional browser workbench and localhost state service; classroom data should be reviewed for privacy before use.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
