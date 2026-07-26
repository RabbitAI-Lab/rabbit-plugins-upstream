## Description: <br>
Audits an email program or planned send with the SEND framework, checking authentication, consent, opt-out, engagement, lifecycle fit, claims, and outcome evidence before release. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, lifecycle, and deliverability teams use this skill to audit an email campaign or program before release. It helps verify SEND criteria, identify unknown evidence, and report whether available controls support a ship, fix, block, or undecided outcome. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The auditor needs campaign, provider, consent, suppression, engagement, and outcome evidence that may be sensitive. <br>
Mitigation: Install only when that evidence can be provided appropriately, and review any proposed persistent audit artifact before authorizing the write. <br>
Risk: Incomplete evidence can be mistaken for approval to send. <br>
Mitigation: Keep missing records as Unknown, list each missing qualified item, and avoid a ship verdict when the required program evidence or scorer is unavailable. <br>
Risk: An audit workflow could accidentally change email, consent, claim, provider, or cache state. <br>
Mitigation: Use the skill for reporting only unless separate explicit approval is given; do not mutate provider settings or execute a send during the audit. <br>


## Reference(s): <br>
- [Standalone Auditor Runtime](artifact/references/auditor-runtime.md) <br>
- [Publisher homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/email-quality-auditor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown audit report with structured status, verdict, score state, missing inputs, findings, controls, and fix owners.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce a permissioned persistent audit artifact only after explicit authorization.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
