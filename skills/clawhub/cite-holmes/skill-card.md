## Description:

Cite Holmes is a deep-research skill that calibrates scope, plans iterative searches, verifies citations with five verdicts, and reports conclusions with confidence grades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, and developers use this skill for structured web research, fact checking, and citation verification. It helps agents produce Markdown research reports that separate verified evidence, partial support, unreachable sources, invalid references, and open research gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad research-style prompts can activate web search, page fetching, and local verification report writing.

Mitigation: Invoke the skill explicitly for research or fact-checking tasks and narrow the scope before allowing broad web research.

Risk: Limited search budget, network failures, or unreachable sources can leave gaps in citation verification.

Mitigation: Keep unverified or unreachable citations out of conclusions and review the verification report before relying on the output.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Cite Holmes publisher profile](https://clawhub.ai/user/docsor1212)
- [Report template and reference schema](references/report-template.md)
- [Search strategies](references/search-strategies.md)
- [Nature article on invalid AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)
- [SkillHub mirror](https://skillhub.cn/skills/cite-holmes)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown reports with citation tables, confidence labels, and optional shell commands for reference verification]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish verified, partial, unreachable, invalid, and unverified citations; QUICK mode uses up to 6 searches and FULL mode uses up to 15 searches.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
