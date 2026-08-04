## Description: <br>
招采文件萝卜坑识别专家（招标人版） helps tenderers and procurement agents review draft tender documents before publication, identify clauses likely to trigger challenges or complaints, and produce risk ratings, legal-anchor directions, rewrite suggestions, response preparation, and reasonableness notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tenderers, procurement agents, and compliance reviewers use this skill to perform pre-publication self-checks on tender documents, focusing on exclusionary, discriminatory, or over-narrow requirements. It produces triage-style compliance findings, practical rewrite suggestions, lawful challenge-response preparation, and supporting rationale for requirements that may be reasonable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and procurement documents may contain sensitive business information. <br>
Mitigation: Use the skill only on documents intended for review and follow the organization's data-handling requirements. <br>
Risk: Legal references, procurement rules, and compliance interpretations may be outdated, incomplete, or jurisdiction-specific. <br>
Mitigation: Verify cited legal anchors against current official sources and consult qualified legal counsel for material compliance decisions. <br>
Risk: The output may overstate or understate risk if the supplied tender document, project type, or procurement need is incomplete. <br>
Mitigation: Provide the complete tender document and project context, then treat findings as triage that requires human review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-carrot-pit-tenderer-1-0-0) <br>
- [Compliance signals reference](artifact/references/compliance-signals.md) <br>
- [Legal anchors reference](artifact/references/legal-anchors.md) <br>
- [Compliance self-check report template](artifact/templates/compliance-selfcheck-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with risk tables, rewrite suggestions, challenge-response preparation, reasonableness notes, and optional local parsing commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are compliance triage and drafting support, not legal advice; legal citations and current validity should be verified before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact manifest declares 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
