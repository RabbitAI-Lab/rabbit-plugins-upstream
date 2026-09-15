## Description:

PRTG Classic (paessler.com). Use this skill for ANY PRTG Classic request: searching and reading device and sensor data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to query PRTG Classic devices and sensors through the OOMOL `prtg_classic` connector without directly handling raw PRTG tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run remote installer scripts without verification.

Mitigation: Review or replace the oo CLI setup with a signed, checksum-verified, or trusted package-manager installation path before installation.

Risk: Connector access depends on OOMOL and PRTG Classic account scopes.

Mitigation: Confirm account scopes are limited to the intended read-only device and sensor tasks before running the skill.

## Reference(s):

- [PRTG Classic homepage](https://www.paessler.com/prtg)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-prtg-classic)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; listed actions read PRTG device and sensor data.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
