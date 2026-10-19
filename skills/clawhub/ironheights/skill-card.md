## Description:

Helps agents review OpenClaw skills for suspicious instructions using local Ironheights scans and explains the findings before the user decides whether to trust them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to review installed or newly downloaded skills for suspicious content, understand scan results, and decide whether to proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The npm package and its update path introduce supply-chain exposure.

Mitigation: Install from the documented source, avoid unpinned npx use where possible, and review updates before trusting them.

Risk: Automatic version checks may contact external services and change installed code.

Mitigation: Set IRONHEIGHTS_NO_UPDATE=1 if automatic checks are unwanted, and rescan skills after updates.

Risk: An incomplete scan or a no-findings verdict can leave malicious content undetected.

Mitigation: Review skipped files and treat scan results as advisory rather than proof of safety.

## Reference(s):

- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Ironheights CLI source and releases](https://github.com/Frank-Masciopinto/ironheights)
- [Ironheights on ClawHub](https://clawhub.ai/frank-masciopinto/skills/ironheights)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with plain-language scan findings and recommended next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory only; incomplete scans and no-findings results do not establish safety.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
