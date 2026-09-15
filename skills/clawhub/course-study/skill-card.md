## Description:

course-study helps an agent write Chinese per-lecture companion notes from official course slides, preserve exam-evidence labels, update a course memory bank, answer follow-up questions on stored concepts, and produce end-of-term summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincentjiang06](https://clawhub.ai/user/vincentjiang06)

### License/Terms of Use:

MIT

## Use Case:

Students and study-focused agent users use this skill to turn each new lecture PDF into a structured Chinese companion document, keep course concepts in a persistent memory bank, and later summarize or reorganize the course from that stored knowledge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The README recommends an unpinned npx installer that can execute code outside the reviewed artifact.

Mitigation: Install from a trusted revision, use the local copy method, or use a pinned and verified installer before deploying the skill.

Risk: Normal use creates and updates course study files, including study/伴读, study/记忆库, and related study documents.

Mitigation: Run the skill in the intended course folder and review planned file changes before accepting them.

Risk: The skill generates study guidance and exam-angle labels from provided course material, which can be incomplete if the course evidence is incomplete.

Mitigation: Provide official lecture PDFs, syllabi, and past-paper or homework evidence when available, and review generated notes before relying on them for exam preparation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/course-study)
- [Skill specification](SKILL.md)
- [English README](README.en.md)
- [Chinese README](README.md)
- [Companion-writing rules](rules/companion.md)
- [Formatting and math rules](rules/format.md)
- [Course memory rules](rules/memory.md)
- [Summary rules](rules/summary.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown files and concise conversational answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Chinese study material with English technical terms preserved; may create or update study/伴读, study/记忆库, and related study files in the course folder.]

## Skill Version(s):

4.1.0 (source: SKILL.md frontmatter, CHANGELOG.md, and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
