## Description:

Helps agents reduce hallucinations by requiring evidence for claims, checking data, auditing outputs, and monitoring long-running work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deyogaid](https://clawhub.ai/user/deyogaid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users apply evidence checks to claimed actions and reported data, use independent audits for critical results, and monitor long-running tasks for signs of unsupported progress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Layer 3 can stop an active agent after a single missing-file check without checking whether interruption is safe.

Mitigation: Before enabling Layer 3, add a verification step and a safe stopping checkpoint.

Risk: Cross-model audits may send source content to another provider.

Mitigation: Use a provider approved for the data and exclude secrets or unnecessary private content.

## Reference(s):

- [Cross-Model Audit Prompt](references/audit-prompt.md)
- [Drift Detection Monitor](references/drift-monitor.md)
- [Hallucination Taxonomy](references/taxonomy.md)
- [ClawHub release](https://clawhub.ai/deyogaid/skills/hallucination-guard)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline code, shell snippets, and reusable prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Procedural guidance and monitoring recommendations; applicability depends on the agent platform and task.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
