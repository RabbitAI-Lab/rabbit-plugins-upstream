## Description:

DCC-CUA routes explicit DCC-CUA requests to a project-owned UI Control stack for bounded desktop and browser UI automation with a fail-closed provider boundary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use DCC-CUA when a task explicitly requires the project-owned DCC-CUA route for desktop, browser, or DCC application UI actions. The skill guides target binding, scoped sessions, observation, action, verification, and fail-closed handling when the route is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can drive real desktop or browser UI, which can affect user accounts, purchases, security settings, or permission boundaries.

Mitigation: Keep authorizations task-specific, bind only the exact intended target, and require direct human control for login, purchase, account-security, CAPTCHA, or unexpected permission prompts.

Risk: A failed or unavailable DCC-CUA route could lead to accidental use of a different UI automation provider.

Mitigation: Fail closed: repair the project route only when authorized, otherwise report the blocker and stop rather than substituting a generic computer-use provider.

Risk: Stale observations or changed target identity can cause UI actions to be applied to the wrong state or window.

Mitigation: Preserve process and window identity, treat target changes as a fresh binding, take fresh observations before state-dependent actions, and verify the final state after mutation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-cua)
- [DCC-CUA source skill](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-cua/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and structured route-attestation text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires exact target binding, fresh observations before UI actions, and final-state verification.]

## Skill Version(s):

0.19.99 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
