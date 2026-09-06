## Description:

A Chinese content-writing workflow skill that helps a knowledge creator re-explain a familiar concept by locking the core question, definition, theory target, and analogies before drafting, then preparing a spoken draft and publishing follow-up checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill to turn a familiar business or knowledge-work concept into a Chinese short-form spoken draft. It emphasizes early concept validation, source-checking for theories, red-line review, title and cover coordination, and post-publication measurement planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read or modify local content-production vault files, drafts, brand materials, and publishing follow-up records.

Mitigation: Install and run it only in workspaces where those files are intended to be accessible and editable by the agent.

Risk: Broad concept-explanation prompts may activate the workflow unexpectedly.

Mitigation: Use explicit routing or review activation before applying it in workspaces that contain unrelated writing projects.

Risk: The workflow depends on local rule files and vault paths that may be missing in another workspace.

Mitigation: Confirm the referenced rules, templates, and vault paths exist before using the skill for production drafting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-concept)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [锁四样](references/锁四样.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese Markdown with structured review tables, draft text, checklists, and file-update guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for Chinese concept-explanation scripts; may reference local content vault paths and publishing records.]

## Skill Version(s):

0.2.6 (source: server release evidence; artifact frontmatter says 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
