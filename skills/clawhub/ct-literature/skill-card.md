## Description:

Searches public scholarly literature across OpenAlex, Europe PMC, Semantic Scholar, preprint sources, arXiv, and a local guideline corpus, then normalizes and de-duplicates results into an evidence base with a qualitative safety-literature subset.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical-trial practitioners, clinicians, nurses, medical students, and research teams use this skill to build a traceable public-literature evidence base for trial planning, protocol or CSR background, systematic-review scoping, and qualitative published-safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may submit confidential sponsor, patient, trial, or API-key data as search topics or chat text.

Mitigation: Use only public literature topics and configure API keys through environment variables or a local .env file rather than pasting secrets into chat.

Risk: Guideline-mode results can include pointers or records that require official confirmation.

Mitigation: Treat guideline results as leads and verify them against official guideline sources, especially where records are marked retrieved=false or resemble reviews rather than guidelines.

Risk: Published safety-literature output is qualitative and can be mistaken for adverse-event disproportionality analysis.

Mitigation: Use the safety subset only as corroborating literature context and do not substitute it for dedicated FAERS or regulatory signal analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-literature)
- [Project homepage](https://github.com/medstatstar/ct-literature)
- [Standard operating procedure](references/sop.md)
- [Search menu](references/search_menu.md)
- [OpenAlex key guidance](references/openalex_key.md)
- [Cross-database search mode](references/multi-db-search.md)
- [PROSPERO access guide](docs/prospero_access_guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with optional shell commands plus generated JSON, HTML, Excel, BibTeX, RIS, CSV, and Markdown report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local report artifacts in the working directory; network retrieval is limited to public bibliographic APIs and explicitly confirmed bug reports.]

## Skill Version(s):

0.9.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
