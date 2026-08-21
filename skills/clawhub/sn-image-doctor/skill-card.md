## Description:

Environment diagnostic skill for SenseNova-Skills that checks sn-image-base installation, Python dependencies, and required environment configuration, then prompts users to save missing variables to .env and reload the environment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before running other SenseNova-Skills image workflows to validate installation, Python dependencies, and environment configuration. It helps identify missing setup, dependency, connectivity, or configuration issues and provides corrective shell commands or setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic output can print resolved configuration values that may include API keys, tokens, or endpoints.

Mitigation: Run it only in private terminals and avoid shared logs, CI logs, support sessions, or screen shares unless configuration output is removed or confirmed to redact secrets.

Risk: Interactive configuration can save missing environment values to a local .env file.

Mitigation: Review the target .env path and file permissions before saving credentials, and rotate any credential exposed through terminal history or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-image-doctor)
- [sn-image-base/SKILL.md](sn-image-base/SKILL.md)
- [sn-image-base/references/api_spec.md](sn-image-base/references/api_spec.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Terminal text and Markdown documentation with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exits with status 0 when checks pass and 1 when one or more checks fail; may prompt for missing environment values and save them to .env when run.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
