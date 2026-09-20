## Description:

Creates Chinese per-lecture study companion notes from course PDFs, follows the lecture order, marks exam angles with evidence levels, and maintains a local course memory bank for follow-up questions and end-of-term summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincentjiang06](https://clawhub.ai/user/vincentjiang06)

### License/Terms of Use:

MIT

## Use Case:

Students and course assistants use this skill to turn official lecture PDFs into Chinese study companion Markdown, store new course concepts under study/, and later answer follow-up questions or produce course summaries from that memory. It is not intended to produce submit-ready homework answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run a course-local 管理/catalog.py script after writing study files, which can execute untrusted local code.

Mitigation: Use it only in trusted course folders; review that script and explicitly approve exact commands before allowing it to run.

Risk: The skill creates Chinese study-note output and local course memory files under study/.

Mitigation: Use it only where those local files are expected, and review generated or modified study/ files before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/course-study)
- [README.en.md](artifact/README.en.md)
- [SKILL.md](artifact/SKILL.md)
- [rules/companion.md](artifact/rules/companion.md)
- [rules/layout.md](artifact/rules/layout.md)
- [rules/memory.md](artifact/rules/memory.md)
- [rules/summary.md](artifact/rules/summary.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown study notes, memory-bank entries, brief answers, and optional PDF-export commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes course-study artifacts under study/ and may deliver very long lectures one Part at a time.]

## Skill Version(s):

4.2.0 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
