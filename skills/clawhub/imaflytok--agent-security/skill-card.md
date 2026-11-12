## Description:

Security hardening for AI agents. Audit your workspace for leaked secrets, check file permissions, validate API key storage, scan for prompt injection risks, and monitor for unauthorized access patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[imaflytok](https://clawhub.ai/user/imaflytok)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to audit workspaces for exposed credentials, loose file permissions, sensitive files tracked by git, prompt injection risks, and network reachability concerns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports unexplained third-party coordination endpoints and an unrelated onlyflies.buzz reachability probe.

Mitigation: Review before installing and remove or ignore those endpoints unless the publisher clearly explains why they are needed and what data is sent.

Risk: Local audit commands may surface credential paths or secret-like values in scan output.

Mitigation: Run checks only on approved paths and avoid pasting unredacted scan output into agents, logs, or shared tickets.

Risk: The skill asks users to inspect credential and configuration locations.

Mitigation: Limit execution to environments where the operator has authorization to inspect those files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/imaflytok/skills/agent-security)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash and checklist content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local audit commands for secret scanning, file permission checks, git exposure checks, API key age review, and endpoint reachability checks.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
