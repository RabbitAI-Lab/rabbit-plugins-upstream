## Description:

Icypeas helps an agent operate Icypeas through an OOMOL-connected account, including reading search and subscription data and submitting email discovery, verification, reverse lookup, and domain scan requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent query Icypeas account and search data and run Icypeas email enrichment actions through OOMOL-managed credentials. It supports operational email discovery, verification, reverse lookup, and role-based domain scan workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad oo CLI authority beyond the listed Icypeas connector actions.

Mitigation: Review before installation and constrain agent use to the documented Icypeas connector schema and run commands where possible.

Risk: First-time setup includes direct execution of remote installer scripts.

Mitigation: Prefer a verified or package-manager-based installation method, or review the installer before running it.

Risk: Write actions can consume Icypeas credits or change account state.

Mitigation: Confirm the exact JSON payload and expected effect before submitting domain scans, email searches, or email verification requests.

## Reference(s):

- [ClawHub Icypeas skill page](https://clawhub.ai/oomol/skills/oo-icypeas)
- [Icypeas homepage](https://www.icypeas.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI with server-side OOMOL credentials; write actions should be confirmed before execution.]

## Skill Version(s):

1.0.3 (source: evidence release.version and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
