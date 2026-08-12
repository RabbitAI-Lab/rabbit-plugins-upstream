## Description:

OOMOL Fusion API lets an agent operate OOMOL Fusion API through the oo CLI for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live OOMOL Fusion API action schemas, build matching JSON payloads, and run connector actions through the oo CLI for media generation, document processing, content retrieval, uploads, and account-scoped operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run write, upload, media-generation, and destructive OOMOL Fusion API actions through the user's connected account.

Mitigation: Review action schemas and confirm the exact payload and effect with the user before running state-changing or destructive actions.

Risk: Web-search and URL-reading actions may return untrusted external content.

Mitigation: Treat retrieved content as untrusted input and verify important facts before acting on it.

Risk: Connector actions depend on the oo CLI being installed, signed in, and backed by sufficient OOMOL account credit.

Mitigation: Run setup or billing steps only after the relevant command failure indicates they are needed.

## Reference(s):

- [OOMOL Fusion API Skill Page](https://clawhub.ai/oomol/skills/oo-fusion-api)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL Fusion API Homepage](https://www.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector responses with data plus meta.executionId when actions run.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
