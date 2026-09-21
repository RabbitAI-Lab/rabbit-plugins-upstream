## Description:

Deep research that calibrates scope, plans sub-questions, searches iteratively across sources and languages, verifies every citation, and ships confidence-graded reports with verified bibliography exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, analysts, students, and developers use this skill to produce research reports, fact checks, literature reviews, medical evidence lookups, and verified bibliographies where sources are checked before they are cited.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online verification sends citation metadata and URLs to public services and fetches arbitrary citation links.

Mitigation: Use offline structural checks for sensitive reference lists, review network exposure before deployment, and avoid online verification from sensitive internal networks.

Risk: Untrusted redirects may lead verification traffic toward private network services.

Mitigation: Keep the skill in review until redirect-target SSRF validation is fixed, and run online checks only in a constrained network environment.

Risk: Mechanical verification confirms citation existence and consistency but does not prove that a source supports a claim.

Mitigation: Require semantic source review, keep unsupported or unreachable citations in the human-review section, and avoid treating verified status as proof of truth.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [README](README.md)
- [Search strategies](references/search-strategies.md)
- [Report template and citation schema](references/report-template.md)
- [Verification details](references/verification-details.md)
- [Medical evidence mode](references/medical-mode.md)
- [FAQ](references/faq.md)
- [Nature news analysis on invalid AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)
- [GPTZero hallucinated citation report](https://medium.com/@ljingshan6/100-fake-citations-just-slipped-through-neurips-2025-peer-review-5f34f4436560)
- [SkillHub mirror](https://skillhub.cn/skills/cite-holmes)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown research reports, Markdown/HTML verification reports, BibTeX exports, CSV audit ledgers, JSON audit trails, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include citation verdicts, confidence grades, CiteScore, human-review sections, and optional offline or strict verification modes.]

## Skill Version(s):

1.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
