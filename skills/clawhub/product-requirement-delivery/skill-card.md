## Description:

Convert a lightweight product request and related signed-in product pages into a product-confirmed requirements baseline, then publish it as a single Feishu document.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lza357](https://clawhub.ai/user/lza357)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers and delivery teams use this skill to investigate existing product pages, clarify roles, permissions, business rules, exception scenarios, and acceptance criteria, and publish one confirmed Feishu requirements document for downstream development and testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a signed-in browser session to inspect product pages and capture screenshots that include internal product data.

Mitigation: Use it only on pages intended for the requirements review, preserve originals, mask sensitive values, and review captured evidence before publication.

Risk: It can create or update a Feishu document from the confirmed baseline.

Mitigation: Do not publish until the product manager explicitly confirms the baseline, then read back and audit the Feishu document before handoff.

Risk: Recommended or unverified statements could be mistaken for observed product facts.

Mitigation: Keep fact labels such as Observed, User stated, Recommended, and Unverified, and list inaccessible page facts in the final document.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lza357/skills/product-requirement-delivery)
- [Publisher profile](https://clawhub.ai/user/lza357)
- [Feishu requirement delivery contract](artifact/references/deliverable-contract.md)
- [Product requirements baseline schema](artifact/references/fact-source-schema.md)
- [Intake card](artifact/references/intake-card.md)
- [UI evidence rules](artifact/references/ui-evidence-rules.md)
- [Audit manifest example](artifact/references/audit-manifest.example.json)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown requirements baseline, Feishu document content, screenshot annotations, JSON audit manifests, and validation command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires product confirmation before publication and read-back audit after Feishu publication.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
