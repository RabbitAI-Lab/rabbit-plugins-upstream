## Description:

Publish SKILL.md files to ClawHub and diagnose publish failures across the history, ai-custom-skills, and ai-thoughts skill repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to publish ClawHub skills through guarded GitHub Actions workflows and diagnose skipped or failed publishes across the named repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Following the skill may push repository changes and publish skills under the j3ffyang ClawHub account.

Mitigation: Use it only with the named publishing repositories, keep ClawHub tokens in repository secrets or environment variables, and verify workflow owner guards before publishing.

Risk: Incorrect workflow changes or retries could double-publish a skill or create version collisions.

Mitigation: Publish only from the j3ffyang-owned repository copies, keep mirrored repository runs guarded as no-ops, and verify ClawHub API state before retrying failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/publish-skills)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
