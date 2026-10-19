## Description:

Searches Xiaohongshu posts to help compare competitor topics, content angles, and audience response.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, agencies, content teams, and creators use keyword-based Xiaohongshu search results to compare competitors' content strategies and identify examples for further analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the latest npm package may execute unreviewed code with access to the SocialDataX API key.

Mitigation: Use a vetted, pinned package version when possible and approve execution only in a trusted environment.

Risk: Returned post links can contain xsec_token values that may be exposed in shared results or logs.

Mitigation: Keep complete token-bearing links and exported results within trusted channels; avoid publicly sharing logs or exports containing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-competitor-research-v2)
- [SocialDataX API key and product information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summary with relevant post examples and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed examples from interpretation; results reflect the retrieved search pages, not the entire platform.]

## Skill Version(s):

0.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
