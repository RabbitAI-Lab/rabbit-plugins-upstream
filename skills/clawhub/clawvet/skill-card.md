## Description:

Scan a third-party OpenClaw skill with ClawVet and act on its A to F grade before installing or trusting it. Use when the user says "scan this skill", "is this skill safe", "vet/check this skill", "should I install this", "audit my skills", or "clawvet", or hands you a SKILL.md from ClawHub or another untrusted source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use ClawVet to statically inspect third-party skills before installation or trust, review the returned grade and scan coverage, and decide whether to install, investigate, or block.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned `npx` references may fetch a changing package version.

Mitigation: Use a pinned, locally staged ClawVet version before relying on a scan.

Risk: Partial scan coverage means some referenced paths were not resolved, so the scan evidence is incomplete.

Mitigation: Resolve the reported paths and rerun a complete local scan before relying on its verdict.

## Reference(s):

- [ClawVet on ClawHub](https://clawhub.ai/mohibshaikh/skills/clawvet)
- [ClawVet source repository](https://github.com/MohibShaikh/clawvet)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown assessment with a grade, findings, and recommended next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file paths, line numbers, scan coverage, and command examples.]

## Skill Version(s):

0.15.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
