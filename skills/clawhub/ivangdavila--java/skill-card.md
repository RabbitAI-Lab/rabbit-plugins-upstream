## Description:

Provides Java and JVM guidance for writing, debugging, tuning, building, testing, upgrading, and securing Java applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill for Java and JVM implementation, debugging, performance tuning, build troubleshooting, test diagnosis, security review, and JDK migration guidance. It is especially suited to exception triage, memory and thread diagnostics, dependency conflicts, Spring and JDBC issues, and Java 8 to 17/21+ upgrades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read and update Java preference memory under ~/Clawic/data/java/.

Mitigation: Review or delete ~/Clawic/data/java/ if persistent Java preferences are not desired.

Risk: Heap dumps and JVM diagnostic artifacts produced while following the skill's guidance can contain secrets or personal data.

Mitigation: Treat diagnostic artifacts as sensitive, restrict access, and avoid sharing them without review and redaction.

## Reference(s):

- [ClawHub Java Skill](https://clawhub.ai/ivangdavila/skills/java)
- [Clawic Java Skill Page](https://clawic.com/skills/java)
- [Setup and Local Preference Memory](setup.md)
- [Java-Specific Security Guidance](security.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May tailor guidance from Java preference memory stored under ~/Clawic/data/java/ when present.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
