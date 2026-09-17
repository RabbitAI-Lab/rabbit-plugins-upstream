## Description:

Unthread helps an agent operate Unthread account actions through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations agents use this skill to create, retrieve, list, update, and delete external customer accounts in Unthread through OOMOL-managed connector actions. It is suited for account administration workflows where live action schemas and explicit confirmation are needed before state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could run unverified code if copied or executed blindly.

Mitigation: Review the setup path before installation, prefer a version-pinned or package-manager install of the oo CLI, and verify signatures or checksums when available.

Risk: The skill can create, update, or permanently delete Unthread customer account records.

Mitigation: Fetch the live action schema before constructing payloads and confirm the exact target, payload, and effect with the user before write or destructive actions run.

## Reference(s):

- [Unthread ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unthread)
- [Unthread homepage](https://unthread.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and requires confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
