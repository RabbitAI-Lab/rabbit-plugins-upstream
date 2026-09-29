## Description:

AI Commander Management Dashboard. A lightweight companion web UI for monitoring inbound emails received via the email-webhook skill and browser session status created by the browser-auth skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lksrz](https://clawhub.ai/user/lksrz)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to run a local companion dashboard that monitors recent inbound emails from email-webhook and browser session status from browser-auth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dashboard exposes sensitive recent inbound email and browser session status data if reachable by untrusted clients.

Mitigation: Run it only on a trusted machine or network, set DASHBOARD_HOST=127.0.0.1 unless remote access is deliberate, and avoid sharing token URLs.

Risk: The default host can bind to 0.0.0.0, making the dashboard reachable beyond localhost.

Mitigation: Prefer localhost binding or a secured HTTPS/tunnel setup for remote access.

Risk: The browser UI loads third-party frontend code at runtime.

Mitigation: Review the dependency behavior before deployment and prefer packaging frontend assets locally for stricter environments.

## Reference(s):

- [AI Commander Dashboard ClawHub page](https://clawhub.ai/lksrz/skills/aic-dashboard)
- [email-webhook companion skill](https://clawhub.ai/lksrz/email-webhook)
- [browser-auth companion skill](https://clawhub.ai/lksrz/browser-auth)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration details for running a token-gated web dashboard.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Serves read-only dashboard data from local inbox and session files; refreshes the UI periodically.]

## Skill Version(s):

1.8.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
