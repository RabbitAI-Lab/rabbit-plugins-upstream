## Description:

Helps agents assess third-party OpenClaw skills with ClawVet before installation or use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to scan third-party skills, check inspection coverage and findings, and decide whether to install, review, or block them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A global npm install runs scanner code on the user's machine.

Mitigation: Check the published package attestation before installation and update the global package deliberately.

Risk: The optional persistent OpenClaw install gate can block future skill installations.

Mitigation: Enable the gate only with user consent and explain how to disable or remove the policy.

Risk: Remote scans inspect only the fetched manifest, and static scans cannot guarantee a skill is safe.

Mitigation: Stage the full skill locally, confirm inspection coverage, and review findings before relying on a verdict.

## Reference(s):

- [ClawVet on ClawHub](https://clawhub.ai/mohibshaikh/skills/clawvet)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with optional shell and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scan coverage, grade, relevant findings, and an install, review, or block recommendation.]

## Skill Version(s):

0.13.1 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
