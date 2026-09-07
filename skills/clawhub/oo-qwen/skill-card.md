## Description:

Operate Qwen through an OOMOL-connected account for document analysis, OCR, translation, image generation and editing, speech generation, speech recognition, and custom voice workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Qwen action schemas and run matching Qwen actions through the oo CLI for text, image, document, audio, and voice tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code fetched at install time.

Mitigation: Review the installer path first and prefer a pinned, signed, or checksum-verified oo CLI release; avoid running curl-to-bash or irm-to-iex commands in an elevated shell.

Risk: Write and destructive Qwen actions can change or delete account state.

Mitigation: Confirm the exact action payload and target with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Qwen homepage](https://qwen.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qwen)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and metadata when commands are run with --json.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
