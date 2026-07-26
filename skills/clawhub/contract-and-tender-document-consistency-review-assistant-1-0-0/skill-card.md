## Description: <br>
Reviews tender documents, bid responses, award notices, and draft or signed contracts to identify substantive deviations in scope, price, quality, schedule, warranty, payment, and liability terms, then produces an auditable compliance review report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Legal, procurement, audit, and bid-management reviewers use this skill to compare tender, bid, award, and contract documents before or after signing. It highlights red, yellow, and green consistency findings, identifies missing inputs, and recommends remediation for substantive deviations and concealed concessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive tender, bid, award, and contract materials. <br>
Mitigation: Share only the documents needed for the review and avoid unnecessary local write access unless editable output or supervised revisions are intended. <br>
Risk: Cited legal authority or procurement rules may be outdated or jurisdiction-specific. <br>
Mitigation: Verify cited legal authority against official current sources and obtain professional legal or audit review before relying on the report. <br>
Risk: Incomplete inputs can produce misleading consistency findings. <br>
Mitigation: Provide tender documents, bid or award materials, and the draft or signed contract; if any are missing, treat the review as limited until the missing materials are supplied. <br>
Risk: Scanned or image-only documents may not be machine-readable. <br>
Mitigation: Provide OCR text or text-extractable documents before expecting clause-level comparison. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/contract-and-tender-document-consistency-review-assistant-1-0-0) <br>
- [Artifact test cases](artifact/references/test-cases.md) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact-declared homepage](https://github.com/chesaram/my-skill-hub) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown compliance review report with summary, comparison matrix, risk analysis, and remediation recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires tender, bid or award, and contract text for full review; may request missing documents or OCR text before analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
