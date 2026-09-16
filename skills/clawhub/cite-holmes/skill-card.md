## Description:

Cite Holmes guides an agent through calibrated deep research, iterative multilingual search, citation verification, and confidence-graded reporting with optional bibliography and audit exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, writers, and developers use this skill to perform scoped deep research, verify citations and source identifiers, and produce reports whose conclusions are tied to checked references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The verifier makes outbound requests to user-supplied URLs and identifier services.

Mitigation: Run the skill in a sandboxed environment without internal network access, and avoid private, signed, or sensitive URLs.

Risk: Trusted-source verdicts can be influenced by input metadata and do not prove that a source supports a claim.

Mitigation: Require human semantic review for important conclusions and treat verified output as a screening aid, not final authority.

Risk: An unrelated release-gate utility is bundled with the citation-verification package.

Mitigation: Remove the utility before end-user deployment or separately justify and review its network and local-ledger behavior.

## Reference(s):

- [Search Strategies](references/search-strategies.md)
- [Report Template and Reference Schema](references/report-template.md)
- [Medical Mode](references/medical-mode.md)
- [Nature news analysis on AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)
- [Hallucinated citation report referenced by README](https://medium.com/@ljingshan6/100-fake-citations-just-slipped-through-neurips-2025-peer-review-5f34f4436560)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research reports with optional JSON, BibTeX, and CSV verification artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include citation verdicts, confidence grades, human-review sections for unchecked or unreachable sources, and optional verified-only bibliography export.]

## Skill Version(s):

1.6.0 (source: evidence release metadata, artifact/_meta.json, and artifact/scripts/verify_refs.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
