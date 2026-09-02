## Description:

OMEM memory lets an agent use a self-hosted OMEM server to remember facts as beliefs with provenance, detect contradictions instead of overwriting conflicts, check claim state, and show evidence chains for why a belief is held.

This skill is ready for commercial/non-commercial use.

## Publisher:

[troybrandonc-bit](https://clawhub.ai/user/troybrandonc-bit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs durable, auditable memory across sessions for people, entities, preferences, or claims. It is especially suited to workflows that need contradiction detection and evidence-backed explanations before acting on remembered information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remembered facts are stored on the OMEM server configured in OMEM_BASE_URL.

Mitigation: Install and use the skill only with an OMEM server the user intends to run or trust.

Risk: Secrets or credentials could be persisted if they are treated as memory.

Mitigation: Do not store secrets, credentials, or one-off scratch values as remembered facts.

Risk: Acting on contradicted memory can produce incorrect behavior.

Mitigation: Check belief state before acting and ask the user when a claim is CONTRADICTED.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/troybrandonc-bit/skills/omem-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples; helper commands return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OMEM_API_KEY and OMEM_PROJECT; OMEM_BASE_URL defaults to a local OMEM server]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
