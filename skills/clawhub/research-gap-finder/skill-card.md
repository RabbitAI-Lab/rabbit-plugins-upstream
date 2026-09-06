## Description:

Research Gap Finder turns a topic into evidence-bounded, ranked candidate research gaps with source links, candidate research questions, reproducible search provenance, and anti-confabulation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research assistants, and literature-review teams use this skill to run a stdlib-only CLI that queries scholarly APIs, builds local evidence records, and generates candidate-gap reports for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics and search parameters are sent to listed scholarly APIs.

Mitigation: Review topic sensitivity and selected engines before use, and avoid external API queries when the topic or parameters should remain private.

Risk: Generated research gaps can be mistaken for proof that literature is absent or that a topic is novel.

Mitigation: Treat candidate gaps as hypotheses requiring human review, source verification, and novelty cross-checks before research or proposal decisions.

Risk: Retrieved scholarly metadata and generated project records are stored in a local project directory.

Mitigation: Use appropriate local workspace controls and review JSON, CSV, and Markdown outputs before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/research-gap-finder)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [AHRQ Research Gaps](https://effectivehealthcare.ahrq.gov/products/methods-future-research-steps-framework/research)
- [PRISMA-S](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/)
- [OpenAlex API reference](https://help.openalex.org/api/)
- [Semantic Scholar Academic Graph API](https://api.semanticscholar.org/api-docs/graph)
- [Crossref REST access and authentication](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/)
- [Europe PMC RESTful API](https://europepmc.org/RestfulWebService)
- [NCBI E-utilities in depth](https://www.ncbi.nlm.nih.gov/books/NBK25499/)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation)
- [NIST AI 600-1 GenAI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf)
- [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON records and result objects, CSV exports, local configuration/evidence/gap files, and command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate gaps are evidence-bounded hypotheses; generated records retain search provenance, confidence labels, and verification state.]

## Skill Version(s):

2.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
