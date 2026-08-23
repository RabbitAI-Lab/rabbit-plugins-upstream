## Description:

Helps agents create, edit, and verify skills for development automation, data analysis, and workflow orchestration tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to create, update, and verify agent skills, including automation workflow guidance, input/output structure, configuration steps, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks the skill as suspicious because it requests broad development automation authority, including file access, command execution, and possible API credential use.

Mitigation: Run it only in a sandboxed project directory, require explicit confirmation before commands or API calls, and avoid giving it broad credentials.

Risk: The artifact describes command execution, API setup, and file processing workflows that could affect local files or external services.

Mitigation: Review proposed commands, paths, network calls, and generated outputs before applying them to production projects.

Risk: Server-resolved GitHub import provenance is unavailable for this version.

Mitigation: Do not rely on inferred repository provenance; review the provided artifact, ClawHub skill page, publisher profile, and server metadata before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/writing-skills)
- [Homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured text, JSON examples, configuration steps, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed command or API steps that require review before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
