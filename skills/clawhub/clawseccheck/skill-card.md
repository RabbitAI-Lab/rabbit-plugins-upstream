## Description:

Audits a local OpenClaw setup for security misconfigurations, risky skills and prompt-injection exposure, and explains findings and changes over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gl0di](https://clawhub.ai/user/gl0di)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users, developers and administrators use this skill to audit their own agent's configuration, installed skills and local security posture, then review prioritized findings or monitor changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit reads sensitive local configuration, logs, installed skills and credential-store indicators.

Mitigation: Run only on systems you are authorized to audit; use available skip and private controls to limit sensitive inputs.

Risk: Local history and monitoring state can disclose security posture.

Mitigation: Protect local audit files; opt out of history with --no-history or remove stored state with --purge when appropriate.

Risk: A partial audit can miss risks and does not support a full security grade.

Mitigation: Review the reported coverage and missing layers before treating findings as comprehensive.

## Reference(s):

- [ClawSecCheck on ClawHub](https://clawhub.ai/gl0di/skills/clawseccheck)
- [CLI flags](references/cli-flags.md)
- [Frequently asked questions](docs/FAQ.md)
- [Security model](SECURITY_MODEL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational audit summary with optional command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide generation of local reports; an A–F grade requires all five audit layers.]

## Skill Version(s):

4.4.0 (source: frontmatter, server release, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
