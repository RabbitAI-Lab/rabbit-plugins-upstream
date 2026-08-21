## Description:

Baozheng Skills is a PRC-law focused agent skill for legal consultation, complaint drafting, criminal material support, statute analysis, and legal-rule retrieval with official-source lookup preferred and AI knowledge fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and legal-workflow users can use this skill to route Chinese legal questions, generate legal analysis, draft complaint or criminal-support materials, and retrieve or analyze statutes. Outputs are drafts and reference guidance that should be reviewed by a qualified lawyer before filing or relying on them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that the legal deadline calculator can produce dangerously wrong dates, including 60-day periods.

Mitigation: Treat deadline calculations as draft signals only, verify dates against official rules or legal counsel, and fix the calculator before relying on 60-day deadlines.

Risk: The templates may request sensitive identity, financial, and case details.

Mitigation: Minimize data collection, redact full ID numbers, bank records, and third-party personal data where possible, and avoid entering sensitive data unless necessary.

Risk: Generated legal analyses, complaint drafts, and criminal materials could be mistaken for final legal advice or filing-ready documents.

Mitigation: Keep the built-in disclaimers, mark outputs as drafts, and require qualified lawyer review before submission or legal reliance.

## Reference(s):

- [Server-resolved source repository](https://github.com/ebandao777-oss/baozheng)
- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/baozheng)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Legal consultation module](artifact/references/module-a-consultation.md)
- [Complaint drafting module](artifact/references/module-b-complaint.md)
- [Statute analysis and retrieval module](artifact/references/module-c-analysis.md)
- [Criminal support module](artifact/references/module-d-criminal.md)
- [Statute engine guidance](artifact/references/shared-statute-engine.md)
- [Disclaimer guidance](artifact/references/shared-disclaimer.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown responses, legal document drafts, DOCX files, JSON examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve source labels for legal citations, include disclaimers, and treat generated legal documents as drafts for review.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter); ClawHub release 0.1.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
