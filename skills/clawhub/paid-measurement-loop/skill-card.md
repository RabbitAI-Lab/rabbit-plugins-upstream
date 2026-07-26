## Description: <br>
Paid Measurement Loop helps agents read back paid ad campaign changes against a control window and produce a Promote, Keep-testing, Rollback, or Unproven decision with ROAS/CPA math delegated to a separate ROI skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators and analysts use this skill to evaluate paid-ad changes with exported campaign, analytics, and ecommerce data. It normalizes readback windows, attribution, currency, and controls so the agent can produce a decision and handoff summary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local ledger writes may store business performance data without sufficiently clear confirmation or scoped write controls. <br>
Mitigation: Review before installing, use only where local ledger writes are acceptable, and confirm exactly which campaign data should be stored. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/paid-measurement-loop) <br>
- [Publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Skill homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown readback table and handoff summary, with optional shell commands for local ledger recording] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Labels figures as measured, user-provided, or estimated; readback decisions are Promote, Keep-testing, Rollback, or Unproven.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
