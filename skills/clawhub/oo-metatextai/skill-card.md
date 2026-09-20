## Description:

MetatextAI helps agents use the OOMOL-connected MetatextAI connector to list and create guardrail policies, evaluate chat transcripts, and run red-team scans through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators with an OOMOL-connected MetatextAI account use this skill to inspect connector schemas, manage guardrail policies, evaluate chat transcripts, and run selected red-team test scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may run remote pipe-to-shell installation commands for the oo CLI.

Mitigation: Confirm the installation source with the user, prefer OOMOL's official install documentation or a verified artifact, and require explicit approval before running install scripts.

Risk: Write actions can create MetatextAI policies or launch red-team test scans against the connected application.

Mitigation: Fetch the live connector schema first and confirm the exact payload and expected effect with the user before running create_policy or run_test_scan.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-metatextai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [MetatextAI Homepage](https://metatext.ai)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector schema before constructing payloads; write and scan actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
