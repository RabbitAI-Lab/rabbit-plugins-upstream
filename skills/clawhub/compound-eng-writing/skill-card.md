## Description:

Prose editing, rewriting, and humanizing text for natural tone, plus auditing drafts for AI tells without rewriting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and reviewers use this skill to edit human-facing copy, docs, blog posts, emails, PR descriptions, and similar drafts for natural tone. They can also use it to audit AI-writing patterns without asking the agent to make an authorship claim.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Edited output may change factual meaning, citation handling, or the writer's intended voice.

Mitigation: Review corrected text before publishing, with specific attention to factual accuracy, citation integrity, and whether the voice still matches the source draft.

Risk: AI-tell audits may be misread as proof that a person or model authored the text.

Mitigation: Treat audit tags as review evidence only; do not present them as an authorship verdict.

Risk: Substantial rewriting can over-correct prose that already reads naturally.

Mitigation: Use the skill's restraint and changelog workflow to preserve natural sentences and make material edits reviewable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing)
- [ia-writing specification](SPEC.md)
- [Two-phase audit workflow](references/audit-workflow.md)
- [Extended phrase reference](references/phrases.md)
- [PR and MR description style](references/pr-descriptions.md)
- [Before/after examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with edited prose, audit findings, corrected text, and changelog sections when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce corrected prose, short audit tags, rewrite guidance, and PR or changelog copy depending on the request.]

## Skill Version(s):

4.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
