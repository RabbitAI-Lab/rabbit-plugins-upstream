## Description:

A China patent workflow skill for mining patent points, drafting invention, utility model, and design disclosures, reading patents in plain language, monitoring patent-policy changes, and assisting office-action responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomestwei](https://clawhub.ai/user/handsomestwei)

### License/Terms of Use:

MIT-0

## Use Case:

External inventors, patent practitioners, and developers use this skill to turn project materials or patent publications into patent disclosure drafts, readable patent notes, prior-art searches, Obsidian knowledge-base entries, and office-action response drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and write project materials, use web search, and modify an Obsidian vault.

Mitigation: Install it only in workspaces where those actions are acceptable, and review proposed file writes and generated patent or legal content before relying on them.

Risk: Optional office-action embedding setup may store API credentials locally.

Mitigation: Prefer environment variables or an operating-system secret store, avoid command-line API key arguments, and restrict permissions on any secrets file.

Risk: Document-conversion paths may process untrusted DOCX, PDF, SVG, or CAD inputs with known-risk dependency versions.

Mitigation: Pin or update the flagged dependencies before handling untrusted files, and process sensitive inputs in a constrained workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/patent-disclosure-skill)
- [SKILL.md](artifact/SKILL.md)
- [README.md](artifact/README.md)
- [Installation Guide](artifact/INSTALL.md)
- [Tools README](artifact/tools/README.md)
- [Office Action Case Library](artifact/docs/oa/README.md)
- [Obsidian Setup Guide](artifact/docs/obsidian-setup-guide.md)
- [Patent Type Search Reference](artifact/references/patent_type_search.yaml)
- [Patent PDF Sources Reference](artifact/references/patent_pdf_sources.yaml)
- [Patent Domain Rules Reference](artifact/references/patent_domain_rules.yaml)
- [CNIPA Patent Publication Search](http://epub.cnipa.gov.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown drafts, Word-ready Markdown, YAML/JSON configuration, shell commands, and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write disclosure drafts, DOCX-ready files, Obsidian vault materials, SVG/PNG diagrams, and local search or index artifacts when invoked by the agent.]

## Skill Version(s):

3.7.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
