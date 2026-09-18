## Description:

AI Skill Maintainer (EN) guides agents through maintaining published skills, including version updates, bug fixes, feature changes, dependency upgrades, security patches, deprecation, emergency isolation, health checks, and dependency audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to diagnose, patch, publish, deprecate, isolate, and audit ClawHub skills while tracking version, changelog, rollback, and security-review requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad maintenance authority could allow unauthorized modification, publication, deprecation, or isolation of skills.

Mitigation: Install only in a controlled maintainer environment with explicit target skill allowlists, review before publish or deprecation, and audit logs for every write or distribution change.

Risk: Security patch and emergency isolation tasks use caller and authorization values that could be spoofed if the runtime does not enforce identity.

Mitigation: Require runtime-enforced authenticated caller identity and signed approvals for security patch and emergency isolation tasks before allowing writes or distribution changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/ai-skill-maintainer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON, YAML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces maintenance plans, task schemas, review checklists, versioning guidance, command examples, and status-style JSON examples.]

## Skill Version(s):

1.1.0-en2 (source: server release metadata; artifact frontmatter version is 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
