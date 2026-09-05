## Description:

Checks Amazon listing completeness, misunderstanding risks, and supporting review evidence for a fixed listing health audit workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to run a fixed audit/listing health check for an ASIN, review page completeness and misunderstanding risks, and ground recommendations in available review evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform paid reporting, monitoring changes, exports, account-setting changes, and reduced-confirmation flows beyond a narrow listing-health check.

Mitigation: Review the autoConfirm setting and require explicit user approval before confirmed paid actions, monitoring changes, or account-setting changes.

Risk: Review and report data may be exported locally and sent to ari.funewa.com under the user's API key.

Mitigation: Use only intended ASIN and report data, keep ARI_API_KEY out of reports and command examples, and review export destinations before sharing.

Risk: Interrupted paid operations may already have charged credits or generated a report.

Mitigation: Check the existing report or operation status with the provided read/status commands before retrying any confirmed paid operation.

## Reference(s):

- [Skill README](artifact/README.md)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/listing-health)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with CLI command guidance and report links when returned by ARI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ARI API responses as the evidence source; paid operations and monitoring changes require the confirmation behavior described by the skill.]

## Skill Version(s):

1.4.5 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
