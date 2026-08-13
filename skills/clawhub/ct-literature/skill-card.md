## Description:

Searches public scholarly literature across OpenAlex, Europe PMC, Semantic Scholar, preprint sources, and related bibliographic APIs, then normalizes, verifies, de-duplicates, and reports an evidence base for clinical-trial literature questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical-trial practitioners, clinicians, medical students, and developers use this skill to gather published evidence for a drug, disease, method, systematic review, or safety-monitoring question. It supports background research, protocol or CSR introductions, literature surveillance, and qualitative published-safety checks using public sources only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose API keys if they paste real credentials into chat or store them carelessly.

Mitigation: Prefer local environment variables or a local .env file, never include keys in shared chat or documentation, and rotate any key that may have been exposed.

Risk: Topic queries and filters are sent to public bibliographic APIs, which can reveal confidential sponsor, subject, or unpublished project information.

Mitigation: Use only public or non-confidential search topics and remove sponsor-specific, subject-level, or unpublished details before running retrieval.

Risk: The security review flags bundled Coze/ct-advisor strings and open-access PDF claims as potentially stale or unreviewed.

Mitigation: Review package scope and documentation before deployment, and validate any open-access PDF claim against legitimate public sources.

Risk: Published safety literature is qualitative and can be misused as a substitute for quantitative pharmacovigilance analysis or regulatory evidence.

Mitigation: Treat safety-mode output as background evidence only and verify findings against official sources and appropriate safety-analysis workflows before decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Project homepage](https://github.com/medstatstar/ct-literature)
- [Operating SOP](references/sop.md)
- [OpenAlex API key guide](references/openalex_key.md)
- [Multi-database search reference](references/multi-db-search.md)
- [Search menu reference](references/search_menu.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with command examples; generated outputs may include JSON, HTML, XLSX, RIS, BibTeX, CSV, and Obsidian Markdown files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public-source literature retrieval with citation verification, provenance logging, relevance scoring, PRISMA screening, and optional reference-manager exports.]

## Skill Version(s):

0.6.14 (source: server release evidence; artifact frontmatter reports 0.6.1 and artifact changelog top entry reports v0.6.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
