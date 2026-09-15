## Description:

JigsawStack helps agents use the JigsawStack connector for web search, search suggestions, text summarization, translation, profanity checks, and spam checks through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run JigsawStack actions through the OOMOL `oo` CLI for web search, search suggestions, text summarization, translation, profanity detection, and spam detection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote script execution for installing the oo CLI.

Mitigation: Install only if comfortable with OOMOL's hosted installer path, or use a pinned manual installation method with a verified checksum or signature.

Risk: Searches, documents, and text payloads are processed through the external JigsawStack connector service.

Mitigation: Review the data being sent before running connector actions, especially when it may contain sensitive or regulated content.

## Reference(s):

- [JigsawStack homepage](https://jigsawstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected JigsawStack service.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
