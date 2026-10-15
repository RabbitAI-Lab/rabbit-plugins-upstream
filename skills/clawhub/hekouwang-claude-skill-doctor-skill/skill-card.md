## Description:

Audits Agent Skill packages for triggering, structure, portability, and basic safety, then recommends prioritized fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this tool to audit one or more Claude or other Agent Skills, review a scorecard, and prioritize improvements to their instructions and packaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional trigger evaluation may pass untrusted skill descriptions to a live Claude CLI session with inherited access.

Mitigation: Prefer the static check.py workflow; evaluate third-party skills only in a disposable sandbox with minimal environment, least-privileged credentials, and strict tool and network controls.

## Reference(s):

- [ClawHub release](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-skill-doctor-skill)
- [Project homepage listed in ClawHub metadata](https://github.com/huiyonghkw/hekouwang-claude-skill-doctor-skill)
- [Doctor suite guide](artifact/references/doctor-suite.md)
- [Trigger evaluation guide](artifact/references/trigger-eval.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Guidance]

**Output Format:** [Text or JSON scorecard with prioritized recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report on individual skills or scan multiple skill directories; changes to skill files require user approval.]

## Skill Version(s):

1.8.1 (source: ClawHub release, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
