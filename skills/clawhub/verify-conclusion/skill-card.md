## Description:

Use when the agent has just produced a diagnostic conclusion, research finding, or any inference from collected evidence. Systematically stress-tests the reasoning chain and re-derives from scratch to catch premature conclusions, unverified assumptions, and causal fallacies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocketdemon](https://clawhub.ai/user/rocketdemon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to check diagnostic conclusions, research findings, inferences, and remediation plans. It guides a structured review of assumptions and evidence, followed by an independent re-derivation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mandatory diagnostic tests may change databases, interrupt services, or use live credentials without clear user approval.

Mitigation: Review the workflow before enabling it on live systems. Require explicit approval for database changes, disruptive service tests, and authenticated operations with side effects; prefer isolated environments and scoped test credentials.

Risk: Copied diagnostic evidence may contain sensitive information.

Mitigation: Protect any copied diagnostic evidence.

## Reference(s):

- [Verify Conclusion on ClawHub](https://clawhub.ai/rocketdemon/skills/verify-conclusion)
- [Publisher profile: rocketdemon](https://clawhub.ai/user/rocketdemon)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Structured text or Markdown containing reasoning checks, findings, and a conclusion or escalation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No runtime artifacts; output depends on the evidence and tools available to the agent.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
