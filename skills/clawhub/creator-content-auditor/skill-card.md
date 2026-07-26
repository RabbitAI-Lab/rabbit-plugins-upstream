## Description: <br>
Reviews influencer content submissions against campaign briefs, approved claims, disclosure obligations, platform requirements, and STAR criteria to produce a pre-publish audit, SQS-oriented guidance, and creator-ready revision feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, influencer, and creator-operations teams use this skill to review one frozen creator deliverable or defined asset set before publication, amplification, or a payment milestone. It checks brand alignment, claim accuracy, disclosure, creative quality, platform fit, authenticity signals, and required evidence before returning an approval, revision, hold, or needs-input posture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit guidance can affect publication approval or payment milestones. <br>
Mitigation: Confirm the target audit path, submitted artifact contents, brief version, market, platform, and user approval before persisting any audit artifact. <br>
Risk: Creator submissions, captions, metadata, QR codes, and embedded instructions may contain untrusted or misleading evidence. <br>
Mitigation: Treat submitted content as evidence only, lock exact asset and claims versions, and require dated provenance and confidence for scored STAR observations. <br>
Risk: A standalone install without the verified runtime cannot safely compute a final score or gate verdict. <br>
Mitigation: Return NOT_SCORED with no persistent artifact or publish decision until the verified scorer, validator, and typed catalogs are available. <br>


## Reference(s): <br>
- [Standalone Auditor Runtime](artifact/references/auditor-runtime.md) <br>
- [Quality Review Aids](artifact/references/quality-review-aids.md) <br>
- [Content Reviewer Templates, Worked Example, and Checklists](artifact/references/review-templates.md) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/creator-content-auditor) <br>
- [Publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance, Files, Shell commands] <br>
**Output Format:** [Markdown report with structured audit status, STAR item observations, SQS-related scoring state, and optional persisted audit artifact after user approval] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return NOT_SCORED when required runtime, scorer, validator, or evidence is unavailable; persistence requires user approval.] <br>

## Skill Version(s): <br>
19.0.0 (source: frontmatter, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
