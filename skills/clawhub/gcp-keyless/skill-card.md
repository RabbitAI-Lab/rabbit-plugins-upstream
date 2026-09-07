## Description:

Operate Google Cloud without recurring browser OAuth or service-account key files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to select and verify short-lived Google Cloud access routes for agents, including attached GCP service accounts and GitHub Actions Workload Identity Federation. It helps inspect cloud resources without recurring browser OAuth or service-account JSON keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A mutable installer reference or source revision could expose environments with cloud credentials to supply-chain risk.

Mitigation: Prefer a pinned installer version and immutable source revision before installation, especially in environments containing cloud credentials or sensitive files.

Risk: Weak Workload Identity Federation conditions or GitHub environment protections could grant broader Google Cloud access than intended.

Mitigation: Restrict WIF to immutable repository and owner IDs, use protected GitHub environments, and verify the expected service-account identity before accessing the project.

Risk: Adding generic command, script, or shell workflow inputs could turn a reviewed observer workflow into an arbitrary executor.

Mitigation: Keep workflow operations as a narrow typed choice list mapped to reviewed commands, and validate workflow text before use.

## Reference(s):

- [One-time Workload Identity Federation bootstrap](references/bootstrap.md)
- [GCP keyless observer workflow](assets/gcp-keyless-observe.yml)
- [ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/gcp-keyless)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to run bundled diagnostic and workflow validation scripts that emit JSON.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
