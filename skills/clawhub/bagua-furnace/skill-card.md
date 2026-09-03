## Description:

Bagua Furnace helps an agent turn books, courses, notes, transcripts, chats, webpages, PDFs, images, and short-video links into reusable, source-anchored methodology cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and knowledge workers use this skill to distill dense source material into reusable decision frameworks, thinking models, and methodology cards for later retrieval by advisor-style agents. It is intended for methodology extraction and synthesis, not professional legal, medical, or financial judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill records local method-layer usage signals by default.

Mitigation: Review the signal controls before use and disable local logging if the default local record is not acceptable.

Risk: The skill can persist generated methodology cards and update a local methodology-library index.

Mitigation: Review target write paths and generated cards before relying on them in downstream advisor workflows.

Risk: Cloud synchronization can send method-layer signal data to configured endpoints when explicitly enabled.

Mitigation: Keep cloud sync disabled unless the publisher and endpoints are trusted, and inspect the signal data before enabling upload.

Risk: Proposal approval workflows use local creator tokens and can apply remote-suggested changes to local files.

Mitigation: Use proposal approval only from a trusted creator environment, inspect proposed changes first, keep backups, and rescan changed files before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j-levee/skills/bagua-furnace)
- [Intro](artifact/references/intro.md)
- [Ingestion guide](artifact/references/ingestion.md)
- [Extraction lenses](artifact/references/extraction-lenses.md)
- [Method card schema](artifact/references/method-card-schema.md)
- [Long-text distillation SOP](artifact/references/long-text-distillation.md)
- [Pattern taxonomy](artifact/references/pattern-taxonomy.md)
- [Signals specification](artifact/references/signals.md)
- [Security audit](artifact/references/security-audit.md)
- [Realtime evidence](artifact/references/realtime_evidence.md)
- [Webpage evidence](artifact/references/webpage_evidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown methodology cards with source anchors, optional concise reports, and shell command snippets for ingestion or local management tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write methodology cards and an index under the user's local methodology library; may record local method-layer signal tags by default, with cloud synchronization only when explicitly enabled.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
