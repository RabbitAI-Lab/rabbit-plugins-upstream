## Description:

Helps authors plan, draft, check, and publish serialized novels through a GitHub-based workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and editors use the skill to develop worlds and characters, draft chapters, check continuity, and prepare GitHub releases for serialized fiction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included GitHub release workflow has a command-injection risk with repository write permissions.

Mitigation: Fix the workflow before use: pass tags through an environment variable, validate allowed tag formats, quote shell values, and remove packages:write unless needed.

Risk: Publishing or draft-sync operations can change repository content, especially when checks are bypassed.

Mitigation: Require explicit confirmation before publishing, promoting, syncing, or using --force or --no-check.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/johnsmithfan/skills/novel-serialization-skill)
- [Server-resolved source repository](https://github.com/JohnSmithfan/Novel-Serialization-Skill)
- [Novel-writing method patterns](references/method-patterns.md)
- [Publishing method patterns](references/method-patterns-publishing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown narratives, planning documents, review reports, and publishing instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts and continuity records may be saved as Markdown files; publishing can create Git tags and releases.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
