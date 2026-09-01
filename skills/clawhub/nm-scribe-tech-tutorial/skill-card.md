## Description:

Plans, drafts, and refines technical tutorials for developers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical writers use this skill to plan, draft, test, and refine hands-on tutorials for libraries, CLIs, APIs, and other developer workflows. It emphasizes scoped outlines, runnable examples, expected output, progressive complexity, troubleshooting, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tutorial drafts may propose commands that install packages, start services, or modify files.

Mitigation: Review generated commands before running them and verify tutorial steps in a clean shell or container.

Risk: Untested code snippets or guessed output can mislead readers.

Mitigation: Run each reader-facing snippet in the target environment and mark any untested platform-specific examples clearly.

## Reference(s):

- [Scribe plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with code blocks, checklists, and structured tutorial sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tutorial outlines, runnable snippets, expected output, troubleshooting sections, and quality gate checklists.]

## Skill Version(s):

1.9.19 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
