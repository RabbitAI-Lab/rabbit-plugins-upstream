## Description:

Investigates genuine research gaps in scientific literature by combining gap-identification frameworks, citation tools, academic databases, bibliometric methods, and a step-by-step workflow that outputs classified, ranked, citation-backed gap reports with candidate research questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, PhD students, labs, and agents use this skill to turn a broad research topic into an evidence-backed state-of-the-field brief, ranked research-gap list, and candidate research questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private manuscripts or unpublished reference sets may be exposed if users submit them to third-party scholarly tools.

Mitigation: Use only accounts, services, and browser automation that match the user's privacy requirements and the service terms; avoid uploading sensitive unpublished material unless approved.

Risk: AI-assisted gap suggestions can be incorrect, incomplete, or based on unresolved citations.

Mitigation: Require DOI or title resolution through Crossref or scholarly APIs, label confidence, cap unverified AI-assisted findings at Medium confidence, and mark unsupported ideas as exploratory.

Risk: Browser automation against citation-mapping tools may conflict with service terms because many tools do not provide public APIs.

Mitigation: Guide the human user through browser-based tools or automate them only where the tool's terms and the user's access permit it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/research-gap-finder)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Companion resource catalog](artifact/resources.md)
- [AHRQ framework for determining research gaps](https://www.ncbi.nlm.nih.gov/books/NBK126702/)
- [Semantic Scholar API](https://api.semanticscholar.org/)
- [Crossref API](https://api.crossref.org/)
- [OpenAlex API](https://api.openalex.org/)
- [PubMed E-utilities](https://eutils.ncbi.nlm.nih.gov/)
- [arXiv export API](https://export.arxiv.org/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, text]

**Output Format:** [Markdown guidance with structured gap-report sections, evidence matrices, citation checks, and optional shell commands for scholarly API queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a citation-backed gap report containing gap statements, gap types, source evidence, importance scores, confidence labels, and candidate research questions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
