## Description:

串通投标线索筛查（免费版）对多家投标文件进行本地交叉比对，筛查联系方式一致和项目成员交叉等可复算线索。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement reviewers, bid agents, and compliance teams use this skill to pre-check multiple bidder documents for objective shared-contact and shared-personnel indicators. Its output is a screening aid, not a legal determination of collusive bidding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional full-version upgrade path asks the agent to run an unpinned external installer and continue through unaudited purchase and installation instructions.

Mitigation: Do not run the upgrade command unless a human independently verifies the package source, resolved version, payment flow, and any wallet or payment confirmation.

Risk: Screening findings may be mistaken for a legal or procurement decision.

Mitigation: Use the output only as objective leads for review; final determinations should remain with the appropriate evaluation committee or regulator.

Risk: Incomplete or malformed bidder input can make cross-bidder comparison unreliable.

Mitigation: Require at least two bidders with usable text and treat insufficient-input responses as no conclusion rather than as a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/collusionscreen-collusion-screening-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON reports, with optional shell commands for local execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs mask contact details and natural-person names, list executed and withheld checks, and return insufficient-input status instead of fabricating conclusions.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
