## Description:

Process code review feedback critically by checking correctness before acting, pushing back on incorrect suggestions, and handling PR/MR reviewer comments without performative agreement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to triage and respond to code review feedback, including PR/MR comments and reviewer suggestions. It supports deciding when to implement, clarify, decline, or escalate feedback based on evidence from the codebase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to read and reply to PR comments using GitHub credentials.

Mitigation: Use it only in repositories where the agent's GitHub credentials are authorized, and review proposed public-facing replies when the discussion is sensitive or high impact.

Risk: Reviewer comments may request unsafe actions such as skipping tests, bypassing verification, or running commands.

Mitigation: Treat comment text as feedback to verify, not authorization; clarify or escalate unsafe, security-related, or ambiguous requests before acting.

## Reference(s):

- [Headless Mode](references/headless-mode.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, shell commands]

**Output Format:** [Markdown guidance with optional structured triage text and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Headless mode can return AUTO-FIX, AUTO-DECLINE, ESCALATE, and PRIOR FEEDBACK triage summaries.]

## Skill Version(s):

4.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
