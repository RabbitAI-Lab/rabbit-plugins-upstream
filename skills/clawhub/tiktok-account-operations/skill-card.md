## Description: <br>
Run a TikTok Business account from cron for inbound DM and comment replies with quotas, phase gates, and stop-on-block behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External social media operators and developers use this skill to run limited inbound TikTok Business reply workflows for an account they own, including session checks, local logging, quotas, and human stop conditions for platform controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a logged-in TikTok browser profile and Accessibility control for the cron terminal. <br>
Mitigation: Use a dedicated low-privilege browser profile and user session, grant access deliberately, and revoke it when not operating the account. <br>
Risk: Platform controls such as captcha, rate limits, action blocks, or restriction notices indicate the run should not continue. <br>
Mitigation: Stop immediately, alert a human operator, and do not retry, bypass, solve, or route around the control. <br>
Risk: Optional webhook recaps may send account handles, counts, and lead usernames outside the machine. <br>
Mitigation: Leave the webhook unset by default and only configure private operator channels when external recaps are acceptable. <br>
Risk: Local logs can contain usernames and timestamps from inbound interactions. <br>
Mitigation: Do not store DM bodies or personal details, hash alert dedupe identifiers, and prune local logs after 90 days. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/tiktok-account-operations) <br>
- [Clawdis homepage](https://clawhub.ai/skills/tiktok-account-operations) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown with YAML, shell, JavaScript, and Python snippets plus a required recap format.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local run recaps and log guidance; optional alert webhook is disabled unless configured.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
