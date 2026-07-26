## Description: <br>
Identifies prohibited related-party bidding among tenderers using public business-registration data, including shared responsible persons, controlling relationships, management relationships, equity penetration, overlapping personnel, shared addresses, and shared contact details, while producing review support rather than a legal determination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement reviewers, compliance teams, and bid-evaluation support staff use this skill to screen multiple bidders for legally relevant business-registration relationships before or during tender review. It helps surface evidence-backed findings and data gaps while keeping final determinations with the evaluation committee or regulator. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may over-treat the generated procurement review report as a legal decision. <br>
Mitigation: Present outputs as review support only and require final determinations by the bid-evaluation committee, regulator, or qualified legal reviewer. <br>
Risk: Business-registration review can involve personal names, contact details, or sensitive procurement materials. <br>
Mitigation: Use redacted or public business-registration data where possible, avoid unnecessary personal details, and follow applicable privacy and procurement-confidentiality rules. <br>
Risk: External business-data or knowledge-base references may be unavailable, unauthorized, incomplete, or inconsistent with the built-in legal posture. <br>
Mitigation: Use only authorized and verifiable external sources, cite their source in findings when provided, and record unresolved or conflicting information in data gaps for human review. <br>
Risk: The skill can be misapplied to bid-behavior or collusion indicators outside its business-registration boundary. <br>
Mitigation: Keep analysis limited to business-registration evidence and route IP, MAC, bid-price, bid-document, deposit, and other behavior-trace questions to a dedicated collusion-analysis process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-related-party-expert) <br>
- [IMA knowledge-base review strategy](artifact/references/ima-kb.md) <br>
- [Equity-penetration data guidance](artifact/references/equity-penetration.md) <br>
- [Test cases and acceptance criteria](artifact/references/test-cases.md) <br>
- [Example end-to-end dialog](artifact/references/example-dialog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [XML report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes summary, findings, network analysis when applicable, data gaps, and recommendations; outputs are procurement review support only.] <br>

## Skill Version(s): <br>
1.1.2 (source: SKILL.md frontmatter, manifest.yaml, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
