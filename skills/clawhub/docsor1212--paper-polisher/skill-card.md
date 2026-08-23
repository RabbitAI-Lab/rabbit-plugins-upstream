## Description:

Paper Polisher Pro helps agents analyze academic drafts for AI-writing signals, terminology issues, translation smell, metaphor quality, and rewrite opportunities in Chinese or English.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External academic writers, editors, reviewers, and developers use this skill to run local draft checks, generate quality reports, identify terminology issues, and prepare user-reviewed rewrite guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill encourages AI-detection evasion and de-AI rewriting, which can be misused to conceal AI-generated work.

Mitigation: Use outputs as review guidance for transparency, quality, and compliance workflows, and require human approval before applying rewrite changes.

Risk: The artifact includes a web-note update workflow that can modify remote note content and generate PDFs.

Mitigation: Require an explicit target-note confirmation, inspect a diff, and verify the current note version before allowing any PUT update.

Risk: The local-only claim does not cover the web-note workflow, which may send sensitive draft content to a remote note service.

Mitigation: Disable or avoid the web-note workflow for sensitive drafts unless the destination service is approved for that content.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/paper-polisher)
- [Article Review Workflow](references/article-review-workflow.md)
- [Guiwu Hub PDF Pipeline](references/guiwu-pdf-pipeline.md)
- [English AI Pattern Library](references/ai_patterns_en.json)
- [Chinese AI Pattern Library](references/ai_patterns_zh.json)
- [Terminology Database](data/terminology.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local report files and PDF-generation steps when the web-note workflow is used.]

## Skill Version(s):

2.0.0 (source: frontmatter, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
