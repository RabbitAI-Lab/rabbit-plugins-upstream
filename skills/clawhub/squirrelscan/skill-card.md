## Description: <br>
Audits websites with the squirrelscan CLI for SEO, performance, security, technical, content, accessibility, and related issues across more than 230 rules, returning health scores, affected URLs, and actionable recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nc9](https://clawhub.ai/user/nc9) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, site owners, and web teams use this skill to audit live or local websites, review prioritized issues, and plan approved fixes for SEO, performance, security, accessibility, content, and crawlability problems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Website audits can scan live sites and may affect production services if run too broadly. <br>
Mitigation: Use the skill only on sites you own or are authorized to test, start with surface or quick scans, and be careful with full live scans on production sites. <br>
Risk: The skill can help edit local website files after reporting audit issues. <br>
Mitigation: Review each proposed fix batch, approve changes before they are applied, and keep edits small enough to inspect and test. <br>
Risk: Configuration commands can overwrite existing squirrelscan settings. <br>
Mitigation: Avoid `squirrel init --force` unless overwriting the existing config is intended. <br>


## Reference(s): <br>
- [Squirrelscan Website](https://squirrelscan.com) <br>
- [Squirrelscan Documentation](https://docs.squirrelscan.com) <br>
- [LLM Output Format Reference](artifact/references/OUTPUT-FORMAT.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/nc9/skills/squirrelscan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and LLM-optimized audit reports, including compact XML-like text, markdown, JSON, text, HTML, or console output depending on the squirrel command options.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the squirrel CLI in PATH; audit results are stored locally by the CLI and can be exported or compared later.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
