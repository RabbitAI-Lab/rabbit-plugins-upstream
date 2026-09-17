## Description:

Faraday lets agents search and read Faraday account, dataset, scope, target, trait, and usage data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Faraday account information, datasets, scopes, targets, traits, and usage statistics without calling the Faraday API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path directs users to install the oo CLI by executing remote installer scripts.

Mitigation: Review the installer source before use; prefer a verified, version-pinned oo CLI install source with published checksums or signatures.

Risk: Connector actions operate through an authenticated OOMOL-connected Faraday account.

Mitigation: Inspect the live connector schema before each action and explicitly confirm any action that is marked write, destructive, or otherwise appears state-changing.

## Reference(s):

- [ClawHub Faraday Skill](https://clawhub.ai/oomol/skills/oo-faraday)
- [Faraday Homepage](https://faraday.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect live oo connector schemas before constructing Faraday action payloads.]

## Skill Version(s):

1.0.2 (source: artifact metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
