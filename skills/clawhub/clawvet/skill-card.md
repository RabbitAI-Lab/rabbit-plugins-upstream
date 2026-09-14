## Description:

ClawVet helps agents scan third-party OpenClaw skills before installation or trust decisions and report the scanner verdict, findings, and install/review/block call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use ClawVet to evaluate third-party OpenClaw skills from local folders, manifests, or ClawHub slugs before installing or trusting them. It supports skill safety review by returning a grade-driven verdict, the findings behind the score, and the recommended next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on running the external clawvet npm package.

Mitigation: Use a pinned clawvet version when fixed detection rules are required, and verify npm provenance or signatures before running scans.

Risk: Remote or incomplete scans may inspect only a manifest or otherwise miss referenced skill behavior.

Mitigation: Stage the full skill locally and require complete local coverage before relying on a scan verdict for installation.

Risk: The optional gate changes OpenClaw install policy persistently and can fail closed on skills it cannot parse.

Mitigation: Review the printed gate configuration and removal steps before enabling it, and scope blocking behavior with the documented threshold option when appropriate.

## Reference(s):

- [ClawVet ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet)
- [Project repository listed in skill metadata](https://github.com/MohibShaikh/clawvet)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and scanner result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scanner fields such as riskScore, riskGrade, recommendation, finding severity, and file or line locations.]

## Skill Version(s):

0.12.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
