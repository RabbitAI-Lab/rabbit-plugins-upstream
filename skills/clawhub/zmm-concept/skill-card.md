## Description:

Guides an agent through an opinionated Chinese content-writing workflow for re-explaining familiar concepts by locking four key judgments before drafting, then refining through spoken review, red-line checks, and release preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing agents use this skill to develop short-form Chinese knowledge scripts that reframe a common concept, require the human host to supply the core definition, and carry the draft through review, cover/title preparation, and post-release tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read a local content vault and update drafts, indexes, frontmatter, and related records as part of the writing workflow.

Mitigation: Install it only in workspaces where that local content access is intended, invoke it with explicit slash commands for tighter control, and review proposed file changes before accepting them.

Risk: Several workflow steps depend on local rule, template, and review files that are referenced but not bundled in the artifact.

Mitigation: Provide the expected local vault files before use, and treat a missing required reference as a reason to stop rather than continue from memory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-concept)
- [Publisher profile: iamzifei](https://clawhub.ai/user/iamzifei)
- [锁四样](artifact/references/锁四样.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown-oriented agent guidance with draft text, structured checklists, frontmatter/configuration updates, and inline shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or update local draft files, indexes, frontmatter, review tables, cover instructions, and calendar tasks when the referenced workspace paths are available.]

## Skill Version(s):

0.2.2 (source: ClawHub release metadata; artifact frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
