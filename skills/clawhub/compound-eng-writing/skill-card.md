## Description:

Prose editing, rewriting, and humanizing text for natural tone, or auditing a draft for AI tells without rewriting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, developers, and product teams use this skill to rewrite copy, docs, blog posts, emails, and PR descriptions in a more natural voice, or to audit drafts for AI-writing tells without making authorship claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can substantially change tone or remove wording that carries the writer's intent.

Mitigation: Review the corrected text and changelog before publishing, and preserve sentences that already read naturally.

Risk: Readers may overinterpret audit findings as proof that AI wrote a draft.

Mitigation: Use detection output as pattern evidence only; do not score the draft or claim authorship.

Risk: Cleaning copied chat links or citation artifacts can change URLs, attribution, or citation text.

Mitigation: Check cleaned links and citations against the original source material before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing)
- [Specification](SPEC.md)
- [Two-Phase Audit Workflow](references/audit-workflow.md)
- [Extended Phrase Reference](references/phrases.md)
- [PR and MR Description Style](references/pr-descriptions.md)
- [Before/After Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with audit findings, corrected text, changelog entries, or PR description prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detect mode reports writing patterns without scoring or claiming authorship; edit mode preserves the writer's voice and includes a changelog.]

## Skill Version(s):

4.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
