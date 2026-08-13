## Description:

Java Coding Guide Pro helps agents write, modify, refactor, and review Java and Spring Boot code using opinionated guidance for null handling, collections, dates, IO, HTTP, JSON, concurrency, Bean mapping, crypto, logging, money calculations, and JDK 8-25 feature gating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baixuanzhu](https://clawhub.ai/user/baixuanzhu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill as a Java coding standards and review guide when generating, editing, refactoring, or reviewing Java and Spring Boot code. It is especially useful for applying consistent stack-aware recommendations and avoiding common defects in concurrency, date/time handling, cryptography, logging, JSON, Bean mapping, and monetary calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for most Java or Spring Boot coding tasks and broadly influence style choices.

Mitigation: Use it when the team wants this coding guide as the default Java posture; otherwise narrow activation or review recommendations before applying them.

Risk: Coding guidance can be incorrect, outdated, or mismatched to a project's JDK version and existing dependency stack.

Mitigation: Have agents inspect the target JDK and current project dependencies first, then review generated changes and tests before merging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/baixuanzhu/skills/java-coding-guide-pro)
- [01 - Null safety and strings](references/01-null-and-string.md)
- [02 - Collections and Stream](references/02-collection-stream.md)
- [03 - Date and time](references/03-date-time.md)
- [04 - File IO, HTTP, and JSON](references/04-io-http-json.md)
- [05 - Concurrency and thread pools](references/05-concurrency.md)
- [06 - Object mapping and Bean handling](references/06-object-mapping.md)
- [07 - Cryptography and hashing](references/07-crypto.md)
- [08 - Exceptions, logging, random values, and assertions](references/08-exception-logging.md)
- [09 - Modern Java syntax and version gating](references/09-modern-java.md)
- [10 - Floating point and BigDecimal](references/10-bigdecimal.md)
- [11 - Naming and coding conventions](references/11-conventions.md)
- [12 - Cognitive complexity](references/12-complexity.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with Java code examples and occasional dependency or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask a short confirmation before recommending new libraries for high-risk crypto or Bean mapping scenarios when the project lacks an established option.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
