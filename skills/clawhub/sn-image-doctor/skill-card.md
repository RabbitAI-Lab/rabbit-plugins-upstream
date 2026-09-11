## Description:

Environment diagnostic skill for the SenseNova-Skills project that checks sn-image-base installation, dependencies, and environment variables, then helps configure missing required variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose whether a SenseNova-Skills environment is ready before running image-related skills, including installation, dependency, and required API configuration checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic output may expose API configuration when logs are shared.

Mitigation: Review output before sharing logs, avoid support or CI runs with real credentials unless redaction is confirmed, and prefer scoped or temporary API keys.

Risk: The documented credential setup does not fully match the shipped script behavior.

Mitigation: Review generated configuration before use, keep .env out of version control, and verify the expected SenseNova environment variables in the local deployment.

## Reference(s):

- [sn-image-base/SKILL.md](sn-image-base/SKILL.md)
- [sn-image-base API specification](sn-image-base/references/api_spec.md)
- [sn-infographic/SKILL.md](sn-infographic/SKILL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text diagnostics with command-line remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prompt interactively for missing environment variables and may write configuration values to a .env file.]

## Skill Version(s):

2026.9.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
