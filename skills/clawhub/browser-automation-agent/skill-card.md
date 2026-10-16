## Description:

Automates a headed browser to navigate, fill forms, and extract content from authenticated websites.

This skill is for research and development only.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to automate interactions with authenticated websites, including extracting page data and filling vendor forms in a controlled test environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a daily browser profile may expose sensitive accounts, autofill data, and browsing history.

Mitigation: Use an isolated test browser profile without real banking, payroll, admin, or personal accounts.

Risk: Automatically approving permissions and capturing every page may disclose private information.

Mitigation: Require explicit permission decisions and capture only screenshots needed for the authorized task.

Risk: Persisted session cookies may allow later reuse of authenticated sessions.

Mitigation: Do not persist or export cookies without explicit authorization for a narrowly scoped task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/hmahmadcs/skills/browser-automation-agent)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Text and downloaded files, such as CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May capture page screenshots.]

## Skill Version(s):

1.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
