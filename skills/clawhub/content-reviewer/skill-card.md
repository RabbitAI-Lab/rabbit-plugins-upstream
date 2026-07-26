## Description: <br>
Reviews influencer content submissions against campaign briefs, approved claims, disclosure duties, platform requirements, and C3 ART criteria to produce evidence-linked approval or revision feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, compliance, and creator-operations teams use this skill to review a frozen influencer asset before publication, amplification, or payment milestone. It checks brand alignment, message accuracy, disclosure adequacy, claim integrity, creative quality, and platform fit, then returns creator-ready feedback tied to evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review results can affect creator approval, publication, or payment decisions when submission, brief, claim, disclosure, or platform evidence is incomplete. <br>
Mitigation: Require locked asset, brief, approved claims, disclosure facts, platform requirements, market, and observation date before scoring; return Needs Evidence when required inputs are missing. <br>
Risk: Persistent audit files could record an unreviewed or incorrect decision. <br>
Mitigation: Ask for user approval before writing an audit artifact, validate the complete draft, and preserve NOT_SCORED behavior when the verified scoring runtime is unavailable. <br>


## Reference(s): <br>
- [Content Reviewer on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/content-reviewer) <br>
- [Skill homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Standalone Auditor Runtime](references/auditor-runtime.md) <br>
- [Quality Review Aids](references/quality-review-aids.md) <br>
- [Review Templates](references/review-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files] <br>
**Output Format:** [Markdown review report with structured scoring, decision, revision feedback, and optional audit artifact] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Persistent audit artifacts require user approval; unavailable scoring runtime returns NOT_SCORED rather than a gate verdict.] <br>

## Skill Version(s): <br>
17.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
