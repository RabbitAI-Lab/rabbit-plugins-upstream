## Description:

Generates random secure passwords of 12 to 16 characters using uppercase letters, lowercase letters, numbers, and symbols, with optional length and character-set settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill in an agent to generate random passwords with requested length, character-set, or batch-generation constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan verdict is suspicious because the skill asks for broad read, write, and command execution capability for a password generator.

Mitigation: Install only in an agent environment where file access, writes, and command execution are restricted or confirmed by the user; prefer a narrowed version before production use.

Risk: Generated passwords are sensitive secrets that can be exposed through logs, transcripts, or files.

Mitigation: Avoid storing generated passwords in untrusted locations and review any file writes or shared outputs before use.

Risk: The artifact describes unrelated automation, API, file, and command execution behavior beyond password generation.

Mitigation: Treat behavior outside password generation as out of scope and require human approval for commands, writes, or external service use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/password-generator)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Plain text password strings or JSON/Markdown responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include requested length, character set, and batch quantity when the agent applies those options.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
