## Description:

Generates random secure passwords, typically 12-16 characters, with configurable length and character sets including uppercase letters, lowercase letters, numbers, and symbols.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill in an agent conversation to generate individual or batch random passwords with configurable length and character set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release asks for broad read, write, and execute authority and describes unrelated security automation capabilities beyond password generation.

Mitigation: Review before installing, run with the narrowest available permissions, and prefer a password generator variant that does not require exec, write access, or an API key unless those capabilities are explicitly needed.

Risk: Generated passwords are sensitive secrets that could be exposed through logs, shared chat history, or untrusted files.

Mitigation: Avoid logging generated passwords, do not store them in untrusted locations, and move needed passwords directly into an approved password manager or secret store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/password-generator)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Plain text or JSON-style Markdown examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce password strings, password generator settings, or batch password lists based on user-supplied length, character-set, and quantity requirements.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter says 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
