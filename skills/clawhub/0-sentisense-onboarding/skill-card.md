## Description:

Read first when using any SentiSense stock market skill: API key setup and which skill owns each task. Patterns to adapt, not scripts. The user's task always wins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers using the SentiSense stock market skill collection use this guide to configure API key access and choose the skill suited to a market research task. It also explains read-only data access conventions and how to handle limited previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags unpinned `npx sentisense` commands that could run a future package release locally.

Mitigation: Review and pin the package version before using the CLI, restrict its access, or use the documented HTTPS provisioning option where suitable.

Risk: The security scan notes a quote lookup capability outside the stated onboarding purpose.

Mitigation: Review referenced skills and limit requests to the endpoints needed for the user's task.

Risk: The security scan is incomplete because a local path-like reference was unresolved.

Mitigation: Inspect the unresolved reference and repeat the security review before deployment.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [Get a SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/0-sentisense-onboarding)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, API calls]

**Output Format:** [Markdown with inline shell commands and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data access guidance; no project files are written.]

## Skill Version(s):

1.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
