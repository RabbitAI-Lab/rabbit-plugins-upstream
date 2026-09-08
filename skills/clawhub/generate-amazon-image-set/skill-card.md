## Description:

Plans Amazon main, listing, and A+ image sets with product fact locking, slot-level generation briefs, PC/mobile pairing, missing-evidence checks, and QA review when the active agent has the required image capabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssesweb](https://clawhub.ai/user/ssesweb)

### License/Terms of Use:

MIT

## Use Case:

External sellers, marketplace operators, designers, and agents use this skill to plan and review Amazon product image sets without inventing product facts or unsupported claims. It produces structured image slot manifests, generation briefs, device-pairing guidance, missing-evidence findings, and QA status for MAIN, Listing, and A+ assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may add publisher attribution and external profile links to the first response when invoked.

Mitigation: Review before installation and remove the attribution behavior or make it opt-in if promotional output is not acceptable.

Risk: Image-set work may be blocked by missing product facts, unverified dimensions, or unavailable image inspection capabilities.

Mitigation: Use the skill's NEEDS_REVIEW and BLOCKED states, and require confirmed evidence before exact claims, package contents, dimensions, or final qualification.

## Reference(s):

- [Product Input and Fact Lock](references/input-and-facts.md)
- [Slot and Dimension Contract](references/slots-and-dimensions.md)
- [Composition and Device Rules](references/composition-and-devices.md)
- [Generation Brief Contract](references/prompt-contract.md)
- [Quality Review Protocol](references/quality-review.md)
- [已验证案例：4.5 cm 迷你草帽](references/example-mini-straw-hat.md)
- [Amazon A+ design guide](https://sell.amazon.com/blog/a-plus-content-design-guide)
- [Amazon A+ comparison guide](https://sellercentral.amazon.com/help/hub/reference/external/G202102930)
- [Public mini straw hat workflow case](https://www.quietphoenix.top/archives/generate-amazon-image-set)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured tables, status codes, and generation briefs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions and scope, product fact locks, missing-evidence lists, slot manifests, PC/mobile pairing matrices, generation briefs, plan QA, final-image QA, and overall status.]

## Skill Version(s):

1.3.0 (source: server release metadata and SKILL.md version line)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
