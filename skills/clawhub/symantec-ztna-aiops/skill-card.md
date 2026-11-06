## Description:

Use for read-only Symantec ZTNA site and connector health, applications, access policies, collections, DNS, identities, cloud integrations and audit logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

ZTNA administrators and operations teams can use the skill to inspect site and connector health, applications, access policies, DNS, identities, integrations, and audit logs through read-only queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external runtime package and linked setup and verification documents were not available for review, so their security claims remain unverified.

Mitigation: Verify and pin the package before supplying tenant credentials, and use a trusted tenant endpoint with credentials limited to the required read access.

Risk: A health sample may not cover the full tenant, and reported site or application status does not prove end-user connectivity.

Mitigation: Treat results as bounded observations, check relevant sites and applications directly, and confirm connectivity through separate operational checks.

## Reference(s):

- [Agent guardrails](artifact/references/agent-guardrails.md)
- [Project homepage](https://github.com/AIops-tools/Symantec-ZTNA-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/symantec-ztna-aiops)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Text summaries and command-line examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only tenant health, configuration, and audit results; a health sample may not cover the full tenant.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
