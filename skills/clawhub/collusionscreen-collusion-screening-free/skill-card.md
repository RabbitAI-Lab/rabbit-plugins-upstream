## Description:

Compares multiple bidding document texts to surface objective, reproducible collusion-screening leads for shared contact details and overlapping project personnel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, bid reviewers, and bidding-document operators use this skill to pre-screen multiple bidders' document text for mechanically reproducible indicators such as duplicate contact details and shared key personnel. The output is intended as review leads, not as a legal finding or scoring decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bidding documents can contain confidential or personal information.

Mitigation: Process only documents the user is authorized to review; the security evidence reports local-only behavior with no network use or persistence.

Risk: Mechanical matches can be mistaken for a legal conclusion about collusive bidding.

Mitigation: Use the report as leads for human review and legal or committee assessment, not as a final finding or score.

Risk: Insufficient or incomplete input can make cross-bidder comparison unreliable.

Mitigation: Require at least two usable bidder texts and treat insufficient-input responses as no conclusion rather than as a clean result.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/collusionscreen-collusion-screening-free)
- [Free web version](https://www.tokendidi.cn/check)
- [Sample input template](templates/sample.json)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON report with executed checks, withheld checks, masked findings, and insufficient-input messages when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are described as local-only and masked; findings are reproducible leads rather than legal conclusions.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
