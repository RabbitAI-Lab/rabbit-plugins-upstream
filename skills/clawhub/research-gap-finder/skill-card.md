## Description:

Find evidence-bounded candidate research gaps and output a ranked, source-linked report with a candidate research question per gap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and research-support agents use this skill to collect bounded scholarly evidence, classify candidate literature gaps, rank them with transparent criteria, and produce source-linked reports for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and citation-validation requests are sent to public scholarly APIs and cached in the selected project directory.

Mitigation: Avoid sensitive private topics, run the skill in an appropriate project folder, and review or clear generated cache files when needed.

Risk: Outbound request containment depends on declared scholarly API usage, with redirect allowlist hardening identified as an improvement area.

Mitigation: Run with network egress limited to the declared scholarly API hosts when stricter containment is required.

Risk: Candidate gap reports can be mistaken for proof of novelty or absence if confidence and verification labels are ignored.

Mitigation: Treat outputs as candidate cues, require human review, and use web validation plus independent source labels before relying on high-confidence claims.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/orionshaowswmw/skills/research-gap-finder)
- [Evidence and implementation references](artifact/references.md)
- [Research gap resource catalog](artifact/resources.md)
- [AHRQ Research Gaps framework](https://effectivehealthcare.ahrq.gov/products/methods-future-research-steps-framework/research)
- [PRISMA-S search reporting guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/)
- [OpenAlex API reference](https://help.openalex.org/api/)
- [Semantic Scholar Academic Graph API](https://api.semanticscholar.org/api-docs/graph)
- [Crossref REST API access and authentication](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/)
- [Europe PMC RESTful API](https://europepmc.org/RestfulWebService)
- [NCBI E-utilities in depth](https://www.ncbi.nlm.nih.gov/books/NBK25499/)
- [NIST AI 600-1 GenAI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf)
- [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON/CSV project files, and concise CLI status objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs retain query, engine, request URL, identifier, confidence, verification, and cache provenance for review.]

## Skill Version(s):

2.1.2 (source: ClawHub release evidence; artifact frontmatter remains 2.1.1 with no user-facing behavior changes)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
