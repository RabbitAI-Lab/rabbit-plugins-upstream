## Description:

Helps agents mine patentable ideas, draft Chinese patent disclosures for invention, utility model, and design filings, explain patent documents plainly, track policy signals, and assist office-action responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomestwei](https://clawhub.ai/user/handsomestwei)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, inventors, patent practitioners, and technical teams use this skill to turn project materials, patent PDFs, and office-action materials into Chinese patent disclosure drafts, plain-language patent notes, Obsidian knowledge-base entries, policy watchlists, and response drafts for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency and file-processing risks may arise when using DOCX, STEP, SVG, patent PDF, or office-action vector features.

Mitigation: Install only in a controlled project or virtual environment and pin or upgrade dependencies to patched versions before using those features.

Risk: Embedding-backed office-action search can disclose indexed case text to the configured embedding provider.

Mitigation: Use external embedding providers only for text approved for that provider, or skip vector search and rely on tag-based retrieval.

Risk: Command-line API-key handling can expose credentials through shell history or process listings.

Mitigation: Prefer environment variables or host secret storage and avoid passing API keys directly on command lines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/patent-disclosure-skill)
- [Publisher profile](https://clawhub.ai/user/handsomestwei)
- [Patent domain rules](references/patent_domain_rules.yaml)
- [Patent type search mapping](references/patent_type_search.yaml)
- [Patent PDF sources](references/patent_pdf_sources.yaml)
- [Patent Obsidian format](references/patent_obsidian_format.md)
- [Schema references](references/schemas/README.md)
- [Obsidian setup guide](docs/obsidian-setup-guide.md)
- [Office-action tools guide](tools/oa/README.md)
- [Patent reader tools guide](tools/patent_reader/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, DOCX-ready Markdown, YAML or JSON planning artifacts, Mermaid diagrams, shell commands, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local files such as disclosure drafts, Obsidian notes, Canvas graphs, figure plans, and review artifacts when the host agent permits file writes.]

## Skill Version(s):

3.4.0 (source: frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
