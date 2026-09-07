## Description:

Generates bid-data-backed enterprise due-diligence reports for pre-cooperation, contracting, credit, and operational-risk review, including single-company reports and two-company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this skill to review a company before cooperation, contracting, account-term decisions, or supplier selection. The skill gathers company profile, bid activity, partners, competitors, public-risk findings, and optional contact data into a concise due-diligence report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or reuse a Zhiliaobiaoxun account and collect a MAC-address hash for trial registration when no key is configured.

Mitigation: Prefer setting ZLBX_API_KEY before use; if automatic registration is needed, require explicit user consent and confirm the limited device fields before registration.

Risk: The skill stores API credentials under ~/.zlbx/config.json and generated due-diligence reports under the user's home directory.

Mitigation: Restrict local file access, avoid sharing saved reports unintentionally, and remove stored credentials when the skill is no longer needed.

Risk: Generated reports and source links may include signed share links that expose report or record access.

Mitigation: Do not post generated reports or sk links publicly; share only with intended recipients.

Risk: The security summary flags the HTML report renderer for URL escaping risk.

Mitigation: Treat generated HTML reports cautiously, review links before opening or sharing, and prefer Markdown output until the escaping issue is fixed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/enterprise-due-diligence-shuidixinyong)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [API Quick Reference](artifact/references/api-quick.md)
- [Workflow Guide](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto-Registration Flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown report in chat plus optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include cited bid/company records when available, disclose data boundaries, and may write HTML output under ~/zlbx-company-intel-files/.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
