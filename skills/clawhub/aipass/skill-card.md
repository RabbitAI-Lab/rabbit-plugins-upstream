## Description:

Safely use an installed AIPASS app and OpenClaw tool plugin without exposing credentials. The standalone skill contains instructions only and performs no credential operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use AIPASS when an operation needs a credential that must stay out of chat, model context, files, shell commands, logs, and generic tool calls. The skill directs the agent to use installed AIPASS tools for approved credentialed operations and to fail closed when the broker or tool plugin is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed operations can fail open if an agent substitutes shell commands, generic HTTP requests, browser automation, environment variables, or raw credentials when AIPASS is unavailable.

Mitigation: Require `aipass_status` before the first operation and fail closed for missing tools, unavailable brokers, version mismatches, malformed responses, timeouts, or unknown states.

Risk: Users may assume this standalone skill performs credential access or enforcement by itself.

Mitigation: State that the skill is instruction-only and require review of the separate signed AIPASS native app and compatible OpenClaw tool plugin before use.

Risk: Manual web-login flows can expose secrets if the agent observes, scripts, screenshots, or reattaches during login.

Mitigation: Stop automation after `secure_runtime_required` and require the user to complete login manually without placing IDs, passwords, cookies, MFA codes, or passkeys in chat.

## Reference(s):

- [AIPASS ClawHub skill page](https://clawhub.ai/youteacher/skills/aipass)
- [YouTeacher ClawHub publisher profile](https://clawhub.ai/user/youteacher)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls]

**Output Format:** [Markdown guidance with constrained tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instruction-only skill; credential access depends on a separately installed AIPASS native app and OpenClaw tool plugin.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
