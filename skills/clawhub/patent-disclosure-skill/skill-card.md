## Description:

China patents skill for mining patent points, drafting Chinese patent disclosures for invention, utility model, and design cases, converting disclosures into application documents, chaining disclosure-to-application docketing, searching CNIPA bibliographic records, explaining patents, briefing examination-policy changes, and assisting office-action responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomestwei](https://clawhub.ai/user/handsomestwei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, inventors, and patent practitioners use this skill to prepare Chinese patent disclosure materials, application drafts, CNIPA search reports, plain-language patent notes, policy briefs, docket trackers, and office-action response drafts from project materials or patent documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An office-action workflow can automatically install and load an unpinned third-party skill into a global agent skills directory.

Mitigation: Avoid the OA playbook distillation path unless the third-party book-to-skill component is explicitly approved, pinned, and reviewed.

Risk: Confidential invention or office-action material may be exposed if online vector providers are enabled without review.

Mitigation: Use local embeddings or confirm the exact provider and data policy before enabling online vectors.

Risk: The skill can write generated outputs and supporting files into workspace, global skills, Obsidian vault, or local secrets locations.

Mitigation: Run it in a constrained workspace and review writes to global skills, Obsidian vaults, and local secrets files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/patent-disclosure-skill)
- [Publisher profile](https://clawhub.ai/user/handsomestwei)
- [Skill README](artifact/README.md)
- [Installation guide](artifact/INSTALL.md)
- [Patent disclosure workflow](artifact/skills/patent-disclosure/README.md)
- [Patent application workflow](artifact/skills/patent-application/README.md)
- [Patent docket workflow](artifact/skills/patent-docket/README.md)
- [Patent reader workflow](artifact/skills/patent-reader/README.md)
- [Office-action workflow](artifact/skills/patent-oa/README.md)
- [Patent search workflow](artifact/skills/patent-search/README.md)
- [Patent examination policy workflow](artifact/skills/patent-exam-policy/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON/YAML configuration, Word documents, image assets, search reports, trackers, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes user-facing artifacts under workspace output directories such as outputs/patent-search, outputs/patent_reader, outputs/patent-application, outputs/docket, outputs/exam-policy, and outputs/oa.]

## Skill Version(s):

4.5.0 (source: SKILL.md frontmatter and server release evidence, released 2026-09-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
