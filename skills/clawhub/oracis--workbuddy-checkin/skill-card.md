## Description:

Automatically claims daily WorkBuddy check-in credits by using the local WorkBuddy session and the WorkBuddy check-in API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or WorkBuddy users can use this skill to check whether today's daily credits were claimed and to run the idempotent check-in flow manually or on a schedule. It is intended for accounts where the user accepts local credential access for WorkBuddy automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access local WorkBuddy credential files and decrypt an access token.

Mitigation: Install and run it only for accounts where the user explicitly accepts this credential access; do not expose logs or outputs that could contain sensitive credential details.

Risk: The skill can attach a debugger to a running WorkBuddy client and save a reusable local build key.

Mitigation: Run the build-key recovery path only when needed, keep generated at_rest_buildkey.json files private, and remove them when the skill is no longer used.

Risk: Automatic scheduling can repeatedly exercise credential-based account actions.

Mitigation: Use narrow schedules and keep the idempotent status behavior; avoid broad unattended automation unless the user has reviewed the security implications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oracis/skills/workbuddy-checkin)
- [Artifact skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to run bundled Python or Node scripts and report OK, SKIP, INFO, or FAIL status without exposing tokens.]

## Skill Version(s):

1.2.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
