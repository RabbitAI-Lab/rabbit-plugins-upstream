## Description:

Linkfox OS routes cross-border e-commerce requests to LinkFox agents for platform research, market analysis, product selection, listing optimization, product media generation, video generation, compliance checks, sourcing, and uploaded-material workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and developers use Linkfox OS to submit one-shot e-commerce workflows for marketplace data retrieval, market analysis, product selection, listing creation, product media generation, compliance checks, and sourcing research. It is not designed for open-ended interactive chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded product materials, and authentication flows may be processed by LinkFox services.

Mitigation: Use a dedicated LinkFox API key, avoid sending secrets or sensitive personal data in prompts or uploads, and only install the skill when that data sharing is acceptable.

Risk: The onboarding path can involve phone/SMS-code/API-key handling.

Mitigation: Use out-of-band account setup for sensitive accounts when possible, and avoid saving API keys in shell rc files unless the local environment is appropriate for persistent secrets.

Risk: The recharge flow can create payment orders and QR-code payment artifacts.

Mitigation: Review the selected plan, payment method, price, and order details before scanning or sharing a payment QR code.

Risk: Generated share links should be treated as public bearer links.

Mitigation: Share only non-sensitive task results and assume anyone with the link may be able to access the shared output.

## Reference(s):

- [LinkFox OS homepage](https://os.linkfox.com/)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-os)
- [API reference](references/api.md)
- [Agent capabilities reference](references/capabilities.md)
- [Onboarding guide](references/onboarding.md)
- [Onboarding API reference](references/onboarding-api.md)
- [Amazon skills reference](references/skills-amazon.md)
- [Market analysis skills reference](references/skills-market-analysis.md)
- [Product selection skills reference](references/skills-selection.md)
- [Listing skills reference](references/skills-listing.md)
- [Media skills reference](references/skills-media.md)
- [IP and compliance skills reference](references/skills-ip-compliance.md)
- [Third-platform skills reference](references/skills-third-platforms.md)
- [General tools skills reference](references/skills-tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON command results, generated files, and task artifact links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One-shot asynchronous tasks can return HTML reports, JSON datasets, generated media links, uploaded-file virtual paths, payment QR artifacts, and public share links.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
