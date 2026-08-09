## Description:

Write and verify HTML email that renders correctly across email clients by using caniemail.com data to guide markup choices and lint finished templates for rendering issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when building, editing, or reviewing HTML email templates and transactional messages for rendering compatibility across Outlook, Gmail, Apple Mail, and other email clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal use may make an outbound request to caniemail.com and create a local cache of the public dataset.

Mitigation: Use --offline when network access should be avoided, and rely on the bundled dataset snapshot for local-only checks.

Risk: The linter reads any HTML or CSS file explicitly provided by the user.

Mitigation: Run it only on files intended for local compatibility analysis and review the JSON findings before applying changes.

Risk: Compatibility guidance can be affected by cached, bundled, stale, or untested caniemail.com data.

Mitigation: Check data_source, warnings, last_test_date, and staleness fields, and independently test untested or high-impact rendering behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shbernal/skills/email-compat)
- [Publisher profile](https://clawhub.ai/user/shbernal)
- [caniemail.com](https://www.caniemail.com)
- [caniemail.com API data](https://www.caniemail.com/api/data.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON, markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results may identify data_source as live, cache, or bundled and include client-specific compatibility findings.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
