## Description:

Provides a fully offline, single-file WeRead Socratic reading companion with Reader Memory v2 and user-confirmed cross-book relations, to be used only when the user explicitly asks for weread-socrates, WeRead companion reading, or cross-book idea comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users and reading-focused agents use this skill to open a local, read-only HTML companion for manually pasted passages, deterministic Socratic questions, browser-local reading memory, and user-confirmed comparisons across books.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted passages, notes, and confirmed relations can persist in browser localStorage on the machine where the HTML file is opened.

Mitigation: Use it only in browsers where local persistence is acceptable, avoid sensitive material in shared browsers, and clear the browser site data when the memory should be removed.

Risk: User-triggered Markdown or PNG exports may include pasted book excerpts or personal notes.

Mitigation: Review exported files before sharing and keep copyrighted or sensitive reading material for authorized personal study.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/weread-socrates)
- [README](README.md)
- [FAQ](docs/faq.md)
- [Canonical Cases](docs/canonical-cases.md)
- [GEO Evaluation](docs/geo-evaluation.md)
- [GEO Manifest](geo-manifest.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Text and Markdown guidance for a local HTML reading companion, with optional user-triggered Markdown and PNG exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The runtime is a self-contained file:// HTML page using browser localStorage for Reader Memory v2; exports occur only after user action.]

## Skill Version(s):

1.4.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
