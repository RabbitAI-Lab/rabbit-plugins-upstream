## Description:

AOPT is an authorized-use diagnostic toolkit for profiling how an agent runtime responds to a fixed set of operational probes.

This skill is for research and development only.

## Publisher:

[hixss](https://clawhub.ai/user/hixss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and reliability researchers use this skill in authorized development or test environments to run fixed diagnostic checks against an agent runtime and compare pass, block, and error outcomes. It is not presented as a production deployment tool or as a substitute for fuzzing or adversarial generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes an opaque bundled helper that hides probe payloads and attempts to run them through a shell.

Mitigation: Run the skill only in a controlled, authorized test environment after reviewing the publisher and validating the helper binary against the supplied release hash.

Risk: Using the diagnostic against production or unauthorized runtimes could create operational or policy risk.

Mitigation: Limit use to development, hardening, and regression workflows where the operator has explicit authorization and can review diagnostic output before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hixss/skills/zhanxing-aopt-skill)
- [Publisher profile](https://clawhub.ai/user/hixss)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Console text summarizing pass, block, and fail diagnostic results; helper responses are parsed from JSON when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports all-check execution and individual check IDs Z01 through Z20, with an optional dry-run mode.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
