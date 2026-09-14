## Description:

A free local pre-check for tender documents that verifies line-item bid arithmetic and scans bidder text for unreplaced template placeholders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill before tender submission to run a local mechanical self-check of bidder line items and document text. It helps surface arithmetic mismatches and leftover template placeholders, but does not make legal, scoring, or bid-evaluation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat mechanical arithmetic and placeholder findings as legal advice or a final bid-evaluation decision.

Mitigation: Use the output as a pre-submission self-check and keep legal, scoring, and award decisions with qualified reviewers or the evaluation committee.

Risk: Sensitive tender files could be exposed if users choose the optional external web checker instead of the local workflow.

Mitigation: Run the local command-line checker for sensitive materials unless the external webpage has been separately reviewed and trusted.

Risk: Incomplete or malformed inputs can prevent the skill from reaching a useful conclusion.

Mitigation: Provide a bidders array with bidder names, item-level quantity, unit price, amount fields, and bidder text when placeholder scanning is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tenderaudit-full-compliance-free)
- [Optional free web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON audit results from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checks performed, checks withheld, insufficient input, arithmetic mismatches, placeholder hits, and supporting details.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
