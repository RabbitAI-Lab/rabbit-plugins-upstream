## Description:

SKILL2 is a fully local Python credential generator for strong passwords, passphrases, URL-safe tokens and API keys, UUIDs, numeric PINs, and password strength checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[q-ian-l](https://clawhub.ai/user/q-ian-l)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and individual users can use this skill to generate local credentials or evaluate password strength without network access, API keys, or third-party dependencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated credentials are sensitive and can be exposed through terminal logs, shared screens, clipboard history, or copied chat transcripts.

Mitigation: Handle generated values as secrets, avoid logging them, and move them directly into the intended secret store or application configuration.

Risk: Supplying a real password as a command-line argument for strength checking can leave it in shell history or process records.

Mitigation: Use stdin for real password strength checks so the value is not typed as a command argument.

## Reference(s):

- [SKILL2 ClawHub page](https://clawhub.ai/q-ian-l/skills/skill2)
- [ClawHub publisher profile](https://clawhub.ai/user/q-ian-l)
- [ClawHub homepage](https://clawhub.ai)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Terminal text and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated credentials and strength-check results print to terminal only.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
