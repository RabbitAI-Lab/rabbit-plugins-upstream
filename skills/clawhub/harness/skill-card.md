## Description:

Harness enforces stable agent workflows with a five-stage pipeline, pre-execution guardrails, and bounded recovery for failed verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to wrap autonomous or headless agent work with clarify, ground, plan, generate, and verify stages. It is also used to apply destructive-operation guardrails, scope checks, and bounded recovery when verification fails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous or headless use can allow package installs, version pinning, or permission changes to proceed without human review if the runtime policy is too permissive.

Mitigation: Configure the runtime so package installs, version pinning, and permission changes require explicit policy approval or are limited to a known safe environment.

Risk: Agent work can drift outside the user's requested scope or propose destructive operations during plan or generate stages.

Mitigation: Use the built-in denylist, scope checks, and exact-operation authorization requirements before execution.

Risk: Repeated recovery attempts can hide unresolved input, logic, or environment failures.

Mitigation: Keep the retry budget bounded, record the adapt step for each retry, and escalate with a fallback report when the budget is exhausted.

## Reference(s):

- [Pipeline guide](artifact/pipeline.md)
- [Guardrails guide](artifact/guardrails.md)
- [Recovery guide](artifact/recovery.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline text, code, command, configuration, and report sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include clarify resolutions, ground notes, plan deliverables, generated changes, verification reports, guard block reports, retry traces, or fallback reports depending on the selected topic and outcome.]

## Skill Version(s):

0.1.2 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
