## Description:

Double6 PPT CLI helps agents create, fill templates, inspect, verify, and narrowly repair native editable PPTX decks from Markdown, text, structured content, and local authorized images; it does not parse PDF/DOCX content, fetch images online, create image-only or HTML slides, or generate TTS/video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[double6-ai](https://clawhub.ai/user/double6-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and presentation-building agents use this skill to generate native PPTX decks, reuse PowerPoint templates at the object level, and run auditable inspection, verification, and constrained repair workflows before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bootstrap path can run third-party OfficeCLI package scripts.

Mitigation: Install only from a trusted publisher, keep OfficeCLI pinned to the evaluated package, use a dedicated runtime directory, and do not run bootstrap as an administrator.

Risk: Detailed local receipts and logs may include plaintext information from decks or workflow inputs.

Mitigation: Avoid highly confidential decks unless local plaintext artifacts are acceptable, and review the run directory before sharing outputs.

Risk: Untrusted or unusually large PPTX/template files can cause local resource exhaustion.

Mitigation: Use trusted source files where possible and run suspicious or large decks in a constrained local workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/double6-ai/skills/double6-ppt-cli)
- [Project homepage from OpenClaw metadata](https://github.com/double6-ai/double6-skills/tree/main/skills/double6-ppt-cli)
- [Authoring contract](references/authoring-contract.md)
- [Delivery gates](references/delivery-gates.md)
- [Machine contracts](references/machine-contracts.md)
- [Repair policy](references/repair-policy.md)
- [Verification tiers and test report](references/test-report-and-verification-tiers.md)
- [Licenses and upstreams](references/licenses-and-upstreams.md)
- [PPT Master upstream](https://github.com/hugohe3/ppt-master)
- [OfficeCLI upstream](https://github.com/iOfficeAI/OfficeCLI)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON plans, PPTX run artifacts, and validation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local receipts, logs, render manifests, package diffs, and finalized PPTX files during the deck workflow.]

## Skill Version(s):

0.2.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
