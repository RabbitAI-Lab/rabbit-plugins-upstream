## Description:

Multi-modal LLM-assisted iterative QA and fixing workflow for web applications: comprehensive testing, root-cause audit, code-level fixes, regression verification, and evidence-chain reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xburn747](https://clawhub.ai/user/xburn747)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and QA engineers use this skill to run structured web-application smoke tests, compare UI behavior against API truth, investigate root causes, apply code-level fixes, and produce regression evidence reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can include production edits, service restarts, destructive tests, and state restoration steps.

Mitigation: Use only for authorized web-application QA, keep it away from live production data by default, and require explicit user approval before destructive tests, source edits, uploads, service restarts, database restore steps, financial or trading-like actions, or long-term memory updates.

Risk: Broad activation triggers may engage the workflow for generic testing or fixing requests before the target environment and permitted test level are clear.

Mitigation: Confirm the target application, scope, environment, authorization, and allowed test level before executing browser automation, write operations, or backend-impacting checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xburn747/skills/smoke-test)
- [Publisher profile](https://clawhub.ai/user/xburn747)
- [Verification Schemes (V1-V11)](artifact/references/verification-schemes.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JavaScript and shell command snippets; included templates can emit JSON summaries and screenshots.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Templates are configurable per target application through BASE_URL, view lists, forbidden strings, and assertion settings.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
