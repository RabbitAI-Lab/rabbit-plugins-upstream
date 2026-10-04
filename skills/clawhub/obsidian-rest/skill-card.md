## Description:

Helps an agent read, search, create, and update notes in an Obsidian vault through the Local REST API plugin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nj070574-gif](https://clawhub.ai/user/nj070574-gif)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents managing an Obsidian vault can find, read, create, append to, and update notes, including runbooks and logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The examples disable TLS certificate verification, potentially exposing the API key and private notes on untrusted networks.

Mitigation: Use only a controlled endpoint; verify certificates with --cacert or a trusted reverse proxy, and rotate any key previously used over an untrusted connection.

Risk: The skill can read private notes and overwrite or delete notes without requiring confirmation.

Mitigation: Review vault access before installation and confirm the intended note and operation before destructive changes.

Risk: Command-execution examples can trigger actions within Obsidian.

Mitigation: Review command IDs and expected effects before executing commands against a vault.

## Reference(s):

- [Obsidian Local REST API plugin](https://github.com/coddingtonbear/obsidian-local-rest-api)
- [Obsidian Local REST API on ClawHub](https://clawhub.ai/nj070574-gif/skills/obsidian-rest)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report note content, search results, paths, and operation status.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
