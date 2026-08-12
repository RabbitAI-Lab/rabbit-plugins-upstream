## Description:

Connects to a hosted Chinese trademark search platform API for trademark search, detail lookup, export, point-balance checks, module checks, and account-binding guidance through a local Node CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[willeleven](https://clawhub.ai/user/willeleven)

### License/Terms of Use:

Apache-2.0

## Use Case:

External users and agents use this skill to query Chinese trademarks, inspect result details, export selected records, check available points or modules, and guide account binding for the tm.zhengquai.com hosted service.

### Deployment Geography for Use:

Mainland China single-region service; all users are served from the mainland China deployment until an overseas region is available.

## Known Risks and Mitigations:

Risk: Trial-credit or pricing language may be inconsistent across release text and user-facing documentation.

Mitigation: Verify the current trial-credit and pricing terms in the platform UI before relying on credits or cost estimates.

Risk: The platform token authorizes user-level access and paid trademark actions.

Mitigation: Treat the token like a password, keep it out of prompts and screenshots, use HTTPS, and revoke or rotate it if exposed.

Risk: Trademark queries and usage history are processed by the hosted service in mainland China.

Mitigation: Review data residency and compliance terms before sending sensitive queries, especially for users subject to cross-border data-transfer requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/willeleven/skills/chinese-trademark-search-skill)
- [Platform homepage](https://tm.zhengquai.com)
- [README](artifact/README.md)
- [API contract](artifact/API_CONTRACT_EN.md)
- [Data residency](artifact/DATA_RESIDENCY.md)
- [Security notice](artifact/SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON to stdout; agent-facing responses should summarize results, point costs, balances, export status, and platform errors.]

## Skill Version(s):

1.2.0 (source: CHANGELOG and package.json, released 2026-08-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
