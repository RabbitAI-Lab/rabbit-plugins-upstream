## Description:

OOMOL Fusion API (oomol.com). Use this skill for ANY OOMOL Fusion API request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate OOMOL Fusion API connector actions through the oo CLI, including schema discovery, JSON action execution, async task polling, media generation and editing, OCR, transcription, document conversion, and file upload workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands that could execute arbitrary local code.

Mitigation: Install only after trusting OOMOL and reviewing or replacing the CLI setup steps; prefer a verified package or independently inspect the installer before execution.

Risk: Write and destructive connector actions can change, remove, or overwrite data through a live OOMOL-connected account.

Mitigation: Confirm the exact target, action, and JSON payload with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fusion-api)
- [OOMOL Fusion API homepage](https://www.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live action schemas before building payloads and to confirm write or destructive actions before execution.]

## Skill Version(s):

1.0.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
