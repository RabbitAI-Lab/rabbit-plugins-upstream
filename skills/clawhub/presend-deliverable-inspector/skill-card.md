## Description: <br>
Reviews PPT, Word, Excel, PDF, email, and multi-attachment deliverables before sending, then gives a send-readiness decision, must-fix risks, unverified items, and a 30-minute repair plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killsnake01](https://clawhub.ai/user/killsnake01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and business teams use this skill for final pre-send review of reports, proposals, board packs, customer materials, emails, and attachment bundles. It helps decide whether the material can be sent now, needs quick fixes, should be paused, or should be reworked before release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect sensitive business materials, including hidden slides, hidden sheets, comments, notes, and review traces. <br>
Mitigation: Use it only with materials approved for inspection and pass only the files or attachments needed for the send-readiness check. <br>
Risk: Raw extraction helpers can expose inspected content through stdout or shared logs. <br>
Mitigation: Run extraction only in trusted environments and avoid logging or sharing raw helper output when documents contain confidential content. <br>
Risk: The skill can identify source gaps, but it must not invent missing evidence or make commitments for the user. <br>
Mitigation: Keep unresolved facts in unverified items and require user confirmation before adding sources, promises, pricing, legal language, or external commitments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/killsnake01/skills/presend-deliverable-inspector) <br>
- [Context Reading](artifact/references/context-reading.md) <br>
- [Detection Playbook](artifact/references/detection-playbook.md) <br>
- [Error Library](artifact/references/error-library.md) <br>
- [File Type Checks](artifact/references/file-type-checks.md) <br>
- [Output Contract](artifact/references/output-contract.md) <br>
- [Risk Taxonomy](artifact/references/risk-taxonomy.md) <br>
- [Inspection Schema](artifact/schemas/presend-inspection.schema.json) <br>
- [Kimi Work Adapter](artifact/adapters/kimi-work.md) <br>
- [WorkBuddy Adapter](artifact/adapters/workbuddy.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown report with optional structured JSON inspection output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include a send-readiness verdict, context basis, risk weighting, must-fix items, can-keep items, a 30-minute repair route, and unverified items.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
