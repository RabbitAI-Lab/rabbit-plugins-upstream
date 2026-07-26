## Description: <br>
Audits a content library, docs site, or blog for low-quality AI-generated filler, then triages what to keep, enrich, rewrite, or delete. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content, SEO, documentation, and publishing teams use this skill to audit existing content libraries for hollow or trust-eroding AI-assisted content and produce a prioritized remediation plan. It also defines a publishing quality gate to reduce recurrence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Content libraries, analytics, or performance data may include sensitive business information. <br>
Mitigation: Share only data appropriate for the agent context and redact confidential details when needed. <br>
Risk: Delete-or-redirect recommendations could remove useful content if accepted without review. <br>
Mitigation: Review the quoted signals, traffic context, and redirect targets before changing or deleting content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/ai-content-audit) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/ai-content-audit.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown audit report with an inventory table, verdicts, triage plan, and quality-gate checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Per-piece verdicts should cite concrete content signals, and delete-or-redirect recommendations should include reviewable redirect targets.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
