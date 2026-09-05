## Description:

Build verifiable proof that a ClawHub release is live and installable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use this skill after publishing a ClawHub skill to verify GitHub, workflow, registry, moderation, public metadata, and isolated installation evidence before claiming the release is live.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A test install used to prove E4 installability can affect download or install metrics.

Mitigation: Use an isolated directory and record the install time, slug, version, reason, contamination window, and new natural observation baseline.

Risk: Release status can be overstated when GitHub push or workflow success is treated as proof of registry availability.

Mitigation: Require registry metadata, a clean moderation verdict, and isolated installation evidence before claiming the skill is live and installable.

## Reference(s):

- [Release Proof Builder ClawHub Page](https://clawhub.ai/bonniegeng-max/skills/release-proof-builder)
- [Publisher Profile](https://clawhub.ai/user/bonniegeng-max)
- [OpenClaw Publisher Repository](https://github.com/bonniegeng-max/openclaw-publisher)
- [Evidence Levels](references/evidence_levels.md)
- [Verification Commands](references/verification_commands.md)
- [Release Proof Report Template](templates/release_proof_report.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with verification findings and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend an isolated ClawHub install check that should be recorded because it can affect download or install metrics.]

## Skill Version(s):

1.0.3 (source: frontmatter, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
