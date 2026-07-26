## Description: <br>
政采无效投标风险雷达 extracts invalid-bid, qualification-review, responsiveness-review, policy-compliance, and hidden risk points from Chinese government-procurement documents and outputs structured checklists for reviewers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Government-procurement practitioners, bid teams, and compliance reviewers use this skill to screen procurement files before submission for risks that could cause a single supplier's bid or response to be rejected. It produces review aids only and does not make binding legal determinations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Checklist output may be incomplete, outdated, or mistaken and should not be treated as legal advice. <br>
Mitigation: Have qualified procurement or legal reviewers verify each flagged item against the source procurement file and applicable regulations before relying on the checklist. <br>
Risk: Procurement files can contain confidential bid, supplier, or project details, especially when external knowledge-base tools are connected. <br>
Mitigation: Use only approved environments for sensitive documents and avoid sending confidential or proprietary details to unapproved external tools. <br>


## Reference(s): <br>
- [Skill README](README.md) <br>
- [Policy Compliance Reference](references/policy-compliance.md) <br>
- [Hidden Conflict Traps Reference](references/hidden-conflict-traps.md) <br>
- [Checklist Template](assets/checklist-template.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/gp-invalid-bid-risk-radar) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown structured checklist with tables and review notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk levels, legal-basis notes, confidence labels, responsible-party fields, and manual-review markers.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence, SKILL.md frontmatter, and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
