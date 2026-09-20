## Description:

Generates daily Chinese sales-advice or anti-fraud article drafts, checks topics against a local article library, applies compliance self-checks, saves Markdown files, and syncs them into a local HTML article library.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meimei-shoulu](https://clawhub.ai/user/meimei-shoulu)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill to produce daily Chinese sales-content or anti-fraud education posts with repeat-topic checks, platform-safety review steps, and local article-library synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads Markdown files and writes new article and library files in a user-chosen local directory.

Mitigation: Choose a narrow article directory, keep backups for important libraries, and review generated files before publishing or sharing them.

Risk: Generated sales or anti-fraud articles may include sensitive claims, private identifiers, platform-risky prompts, or seasonally inaccurate wording.

Mitigation: Apply the documented compliance self-check before publication, anonymize real people and companies, avoid guaranteed outcomes, and verify time-sensitive wording against the current date.

Risk: The bundled HTML library converter supports a limited Markdown subset.

Mitigation: Use simple headings, paragraphs, and inline bold text, then inspect the HTML library entry after synchronization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/meimei-shoulu/skills/sales-daily-article)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Chinese Markdown article draft with YAML frontmatter, plus optional local HTML library entry]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets about 1000 Chinese characters per article and stores articles under a date-based local directory.]

## Skill Version(s):

1.2.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
