## Description:

skillminer suggests reusable skills from recurring patterns in local OpenClaw memory files, drafting review-only candidates with a local-first runner and an optional external fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to identify repeated work patterns in local memory files and turn approved candidates into draft skills for later review and promotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scheduled local agent reads OpenClaw memory files and writes local review state and pending skill drafts.

Mitigation: Install only when that local access is acceptable, and review generated drafts before promoting them.

Risk: Setting FORGE_RUNNER=claude can send prompt data off host to Anthropic.

Mitigation: Keep FORGE_RUNNER unset unless the off-host data flow is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/robbyczgw-cla/skills/skillminer)
- [README.md](README.md)
- [USER_GUIDE.md](USER_GUIDE.md)
- [CHANGELOG.md](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, local review files, and draft SKILL.md content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts are review-only and written under skills/_pending/ before any manual promotion.]

## Skill Version(s):

0.6.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
