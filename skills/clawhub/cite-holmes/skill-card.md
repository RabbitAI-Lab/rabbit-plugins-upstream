## Description:

Pkg Cite Holmes Claw helps agents perform deep research, verify each citation against registries and source pages, and produce confidence-graded reports with verified bibliographies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and writing assistants use this skill to run scoped research, check whether references are real and reachable, and produce reports where conclusions and citations carry verification status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online research and citation verification may send citation metadata and URLs to third-party verification services.

Mitigation: Use offline mode for confidential manuscripts or internal documents, or run the verifier through an approved sandbox or proxy.

Risk: Arbitrary URL verification creates network-safety risk when checking untrusted references.

Mitigation: Use an allowlist, sandbox, or network proxy before enabling broad URL verification in sensitive environments.

Risk: Broad auto-triggering can start research and verification workflows from common research or fact-checking prompts.

Mitigation: Confirm the intended scope and mode before running full research, especially when prompts may contain private or unpublished material.

## Reference(s):

- [Cite Holmes README](README.md)
- [Verification details](references/verification-details.md)
- [Search strategies](references/search-strategies.md)
- [Report template and reference schema](references/report-template.md)
- [Medical research mode](references/medical-mode.md)
- [FAQ](references/faq.md)
- [Nature news analysis on AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)
- [GPTZero report on hallucinated citations](https://medium.com/@ljingshan6/100-fake-citations-just-slipped-through-neurips-2025-peer-review-5f34f4436560)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown research reports with citation verdict tables, plus optional BibTeX, CSV, HTML, and audit JSON exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CiteScore grades, pre-submission conclusions, verified-only bibliography exports, and per-reference audit trails.]

## Skill Version(s):

1.9.0 (source: server release evidence; artifact README changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
