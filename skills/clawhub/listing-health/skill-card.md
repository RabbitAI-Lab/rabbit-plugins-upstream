## Description:

Checks Amazon listing completeness, misunderstanding risk, and review-backed evidence using the ARI listing-health workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and listing operators use this skill to inspect an ASIN for page completeness, likely buyer misunderstandings, and issues supported by review evidence before making listing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a suspicious verdict because paid remote operations may extend beyond the advertised fixed listing-health scope.

Mitigation: Install only when the publisher is trusted, review the requested workflow and focus before confirmation, and monitor the exact command arguments used for each paid operation.

Risk: The skill stores and uses an ARI API key and can spend account credits after explicit confirmation.

Mitigation: Use the quoted cost review step, require explicit confirmation before running paid commands, and revoke or rotate the ARI key if local storage is no longer acceptable.

## Reference(s):

- [Amazon Listing Health Operation Workflow](artifact/references/operation-workflow.md)
- [Amazon Listing Health API Reference](artifact/references/reference.md)
- [ARI Service](https://ari.funewa.com)
- [ClawHub Listing](https://clawhub.ai/funewa/skills/listing-health)
- [Publisher Profile](https://clawhub.ai/user/funewa)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with optional bash commands and JSON-like CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key, uses fixed audit/listing and ops_audit settings, and runs paid analysis only after quote review and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server release evidence, _meta.json, scripts/ari.py VERSION, and CHANGELOG top entry)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
