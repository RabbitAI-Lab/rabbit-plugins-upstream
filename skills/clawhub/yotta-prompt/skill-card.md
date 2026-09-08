## Description:

Yotta-prompt helps agents clarify vague user requests by offering 2-4 intent directions, asking for goal, scope, output, and constraints, and producing a ready-to-run prompt routed to a matching YottaMeta skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users and agent developers use this skill when a request is vague or the user does not know how to prompt an AI. It structures the request into an executable task and returns a ready-to-run prompt, with optional YottaMeta skill routing and installation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to persistently auto-enable it in future sessions, which may change future assistant behavior without a fresh user decision.

Mitigation: Review the always-load behavior before installation and remove or disable persistent startup-registration instructions unless that behavior is explicitly desired.

Risk: Documented unpinned npx installation commands may install a newer package than the reviewed artifact.

Mitigation: Prefer pinned package versions when installing, especially in production or managed environments.

## Reference(s):

- [Scenario examples](references/scenarios.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-prompt)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-prompt)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or plain text, with optional JSON from the local CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local CLI supports configurable candidate counts and returns intent mappings, installation commands, and self-contained prompt templates.]

## Skill Version(s):

0.1.2 (source: server release metadata; artifact files report 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
