## Description:

DeepL lets an agent operate DeepL through an OOMOL-connected account to inspect connector schemas, check usage, list supported languages, and translate text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run DeepL translation-related actions through an authenticated OOMOL connection, including checking quota, discovering supported languages, and translating text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions can run a remote installer directly in a shell.

Mitigation: Review the install step before use; prefer a signed or package-managed oo CLI install, or download and verify the installer before running it.

Risk: Connector commands depend on an authenticated OOMOL account, a connected DeepL API key, valid scope, and available billing.

Mitigation: Use the setup and recovery steps only after a matching command failure, then retry with the live connector schema before sending payloads.

## Reference(s):

- [ClawHub DeepL skill page](https://clawhub.ai/oomol/skills/oo-deepl)
- [DeepL homepage](https://www.deepl.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
