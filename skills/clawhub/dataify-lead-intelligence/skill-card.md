## Description:

Discover and rank companies that match an ideal customer profile using public company, hiring, and market evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and research teams use this skill to create verification-ready company prospect lists from public evidence. It is intended for organization-level account research, territory planning, and lead qualification, not private personal contact enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release bundles an unrelated Amazon review scraper with implicit invocation enabled.

Mitigation: Review the installed package before deployment and remove or disable unrelated bundled capabilities when only lead intelligence is needed.

Risk: Credential handling weaknesses could expose a Dataify token in logs or local state.

Mitigation: Use only environment-based token setup, avoid pasting tokens into chat or command arguments, and rotate the token if it may have been exposed.

Risk: Running from untrusted resume state files could affect subsequent collection behavior.

Mitigation: Resume only from state files created in a trusted run and inspect unexpected state before continuing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-lead-intelligence)
- [Dataify Token Setup](_dependencies/skills/dataify-task-operations/references/token-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration guidance]

**Output Format:** [Markdown summaries with JSON reports and referenced output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include evidence-backed company rows, qualification scores, missing fields, disqualifiers, and a human-verification queue.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
