## Description:

Helps academic authors self-check AI-writing signals and improve drafts with style, terminology, attribution, and revision guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic authors and editors use this skill to review drafts, identify passages for human revision, and check writing conventions and disclosure needs. Detection scores are advisory, not institutional determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts and directories supplied to the skill may be read, and report or terminology-fix operations may write local files.

Mitigation: Review input and output paths before running batch or --apply operations, and keep a copy of important drafts.

Risk: AI-detection scores can be misleading if treated as definitive authorship findings.

Mitigation: Use scores only to guide human review and follow the institution's disclosure policy.

Risk: Optional model setup writes a model into the user's local cache.

Mitigation: Install the optional model only when its source and local cache location are acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article review workflow](artifact/references/article-review-workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown guidance and command examples; local reports may be JSON, CSV, or HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sentence-level suggestions guide human edits rather than automatically rewriting text.]

## Skill Version(s):

5.2.0 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
