## Description:

将转录稿或文献整理为可独立阅读、可溯源验收的结构化课程，并在用户明确要求时归档课程或提取定制培训方案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

中文内容团队、培训交付人员和法律/AI 实践者可用此 skill 将转录稿、逐字稿或文献整理为 Markdown 课程总览、章节和可验证 manifest。它也支持在明确请求下归档既有课程，或从已验证课程素材中提取面向特定受众和时长的培训方案。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-provided transcripts, documents, and course materials that may contain confidential or personal information.

Mitigation: Point it only at intended input directories, choose output locations deliberately, and review generated manifests or audit files before sharing.

Risk: Archive or move actions can copy or relocate generated course files into a knowledge base.

Mitigation: Run archive or move workflows only after an explicit user request and verify the target directory before execution.

Risk: The local verifier checks objective course-file contracts but does not prove full semantic correctness or factual fidelity.

Mitigation: Treat verifier PASS as a gate for structure only, then complete the documented human review for source fidelity, material coverage, and cross-chapter consistency.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cat-xierluo/skills/course-generator)
- [Source Homepage](https://github.com/cat-xierluo/legal-skills)
- [course-manifest.md](artifact/references/course-manifest.md)
- [course-manifest.schema.json](artifact/config/course-manifest.schema.json)
- [outline_prompt.md](artifact/references/outline_prompt.md)
- [overview_prompt.md](artifact/references/overview_prompt.md)
- [chapter_prompt.md](artifact/references/chapter_prompt.md)
- [extract_prompt.md](artifact/references/extract_prompt.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown course files, JSON course-manifest data, configuration guidance, and local verification shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated courses require deterministic verifier checks plus human semantic review before delivery.]

## Skill Version(s):

2.8.1 (source: ClawHub release evidence, SKILL.md frontmatter, CHANGELOG, released 2026-08-25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
