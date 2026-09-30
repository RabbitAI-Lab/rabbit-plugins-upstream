## Description:

Helps agents plan and route YottaMeta skill combinations, inventory installed skills, and preview, install, or update the skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to choose YottaMeta skill combinations, inspect installed skills, and manage family installs and updates in a selected skills directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation or updates can replace local skills and execute downloaded package code; confirmation and verifier trust boundaries are not fully enforced.

Mitigation: Prefer the host's native install path when available; use pinned versions or a reviewed local copy, preview with --dry-run, and check the destination and skill list before installing.

Risk: Bypassing scans or enabling automatic updates increases exposure to untrusted packages.

Mitigation: Avoid --skip-scan and update --auto unless the package source is trusted; consider testing in a separate skills directory first.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage (listed in ClawHub metadata)](https://github.com/YottaMeta/yotta-skills)
- [Skill orchestration guide](references/orchestration.md)
- [Installation flow guide](references/install-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration instructions]

**Output Format:** [Markdown guidance and commands; optional structured JSON from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Route suggestions do not install skills automatically; install and update commands can change local skill files.]

## Skill Version(s):

0.22.0 (source: server release, skill frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
