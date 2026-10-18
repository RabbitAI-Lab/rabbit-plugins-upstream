## Description:

Automates a headed browser to navigate, fill forms, and extract information from authenticated websites.

This skill is for research and development only.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Users and teams can automate browser interactions and collect information from sites that require login, including vendor portals. The skill's documentation describes its intended use as study or research only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a daily browser profile can expose saved passwords, cookies, and browsing history.

Mitigation: Use an isolated browser profile rather than a daily profile, and limit access to accounts needed for the task.

Risk: Automatic permission grants on arbitrary sites can give websites access beyond what the user intended.

Mitigation: Do not automatically grant permissions; require user approval for each permission request.

Risk: Browser automation on banking, payroll, or administrative sites can affect sensitive accounts and data.

Mitigation: Avoid those sites unless explicitly necessary and approved by the user.

Risk: Saved screenshots and persisted session cookies can disclose private information.

Mitigation: Treat screenshots and cookies as sensitive, restrict access to them, and delete them when no longer needed.

## Reference(s):

- [Browser Automation Agent release](https://clawhub.ai/hmahmadcs/skills/browser-automation-agent)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files]

**Output Format:** [Markdown guidance and browser screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Screenshots and reused session cookies may contain sensitive information.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
