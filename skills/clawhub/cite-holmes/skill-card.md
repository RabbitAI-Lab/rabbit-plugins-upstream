## Description:

Deep research that interrogates its own sources by calibrating scope, searching iteratively, verifying citations mechanically and semantically, and producing confidence-graded reports with verified bibliography exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, researchers, and writers use this skill for deep research, fact checking, literature review, medical evidence lookup, and pre-submission reference verification. It is especially suited to reports where every cited source needs an auditable verification status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference metadata may be sent to public academic services during verification.

Mitigation: For private or pre-publication work, use offline mode, avoid optional API keys or mailto identifiers unless needed, and review the disclosure before installation.

Risk: Local caching may retain citation verdict data on the user's machine.

Mitigation: Use the documented no-cache or refresh-cache controls when cached verification state is inappropriate.

Risk: A reachable source can still fail to support the claim it is cited for.

Mitigation: Use the semantic verification workflow and keep unsupported, contradicted, unreachable, or unverified references in human-review paths instead of treating them as final evidence.

## Reference(s):

- [Cite Holmes ClawHub page](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](references/search-strategies.md)
- [Report template](references/report-template.md)
- [Verification details](references/verification-details.md)
- [Medical mode](references/medical-mode.md)
- [FAQ](references/faq.md)
- [SkillHub mirror](https://skillhub.cn/skills/cite-holmes)
- [Nature news analysis on invalid AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)
- [Reported NeurIPS 2025 hallucinated citation findings](https://medium.com/@ljingshan6/100-fake-citations-just-slipped-through-neurips-2025-peer-review-5f34f4436560)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and command guidance, with optional BibTeX, CSV, HTML, and audit JSON exports from the verifier]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include citation verdicts, confidence grades, human-review sections, and verified-only bibliography artifacts when requested.]

## Skill Version(s):

1.12.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
