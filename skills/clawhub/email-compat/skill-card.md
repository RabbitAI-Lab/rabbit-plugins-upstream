## Description:

Write and verify HTML email rendering across email clients using caniemail.com data, including compatibility checks, linting, client-specific findings, and workarounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, email engineers, and agents use this skill when building, editing, or reviewing HTML email templates and transactional messages. It helps check CSS and HTML support across clients such as Outlook, Gmail, and Apple Mail before treating an email as compatible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool may contact caniemail.com and cache compatibility data locally.

Mitigation: Run with --offline when outbound network access is not allowed, and review cache behavior during deployment.

Risk: Compatibility answers can be stale or based on bundled data rather than live caniemail.com data.

Mitigation: Check data_source, last_test_date, and staleness in results; use --refresh when current data is required.

Risk: The skill covers email rendering compatibility only, not sending mail, deliverability, SPF, DKIM, DMARC, BIMI, list management, or ESP selection.

Mitigation: Use dedicated deliverability and email infrastructure tools for those topics.

Risk: Untested client-feature combinations can be mistaken for support or lack of support.

Mitigation: Treat untested verdicts as unknown and test the target email client directly before relying on the result.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/shbernal/skills/email-compat)
- [Release Changelog](https://github.com/shbernal/caniemail-ai-tooling/releases/tag/v0.2.2)
- [Can I Email](https://www.caniemail.com)
- [Can I Email Data API](https://www.caniemail.com/api/data.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON compatibility or lint results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results include verdicts, affected clients, positions, notes, feature metadata, and data_source.]

## Skill Version(s):

0.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
