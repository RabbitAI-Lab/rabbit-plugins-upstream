## Description:

Provides a Chinese-language LGD checklist and gate assessment for legal AI systems covering registration, evidence, and human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Legal teams and developers of legal AI applications use this local checklist to assess registration, supporting evidence, and review gates before relying on an AI system for research, drafting, or opinion support. It does not replace legal advice or review by a qualified lawyer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A checklist result may be mistaken for legal advice or a definitive compliance finding.

Mitigation: Treat scores as a self-check only; verify current official requirements and obtain qualified legal review for consequential decisions.

Risk: Keyword-based self-assessment can mark a requirement present without verifying its underlying evidence.

Mitigation: Review each cited requirement and its actual supporting documents before accepting a passing gate result.

Risk: Sensitive case or client details may be exposed if optional web or file-writing tools are used unnecessarily.

Mitigation: Keep assessments local by default and use web lookup or report saving only when explicitly needed, with minimized data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-law-ethic)
- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Chinese-language checklist, scores, gate result, and missing items in text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local, deterministic heuristic or supplied-answer scoring; exit status indicates pass, fail, or usage error.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter says 1.1.0 and manifest says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
