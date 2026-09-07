## Description:

Polishes and normalizes Chinese academic writing by reducing colloquial phrasing, maintaining terminology consistency, checking GB/T 7714-2015 citation format, and returning polished text, a change table, and unresolved author-review items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sharinchan233](https://clawhub.ai/user/sharinchan233)

### License/Terms of Use:

MIT-0

## Use Case:

External users, students, researchers, and editors use this skill to polish Chinese academic manuscript passages, standardize academic tone and terminology, and surface facts or data that require author confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Polishing could unintentionally change the author's intended meaning or make an unsupported conclusion sound stronger.

Mitigation: Apply the skill's minimum-change rule, preserve the argument structure, and mark uncertain facts or data as author-review items.

Risk: Citation and reference-format corrections may still require validation against the original sources.

Mitigation: Have the author verify years, pages, reference entries, and GB/T 7714-2015 formatting before submission.

## Reference(s):

- [Chinese Academic Writing Style Guide](artifact/references/style-guide.md)
- [Before and After Example](artifact/examples/before-after.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with polished text, a change-comparison table, and unresolved review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flags uncertain facts, data, sample sizes, p-values, and citation details for author confirmation instead of modifying them.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
