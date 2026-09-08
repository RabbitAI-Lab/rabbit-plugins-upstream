## Description:

UIFlow2 MicroPython coding assistant for writing, debugging, reviewing, and explaining UIFlow2 code for M5Stack devices using bundled official documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuyun2000](https://clawhub.ai/user/yuyun2000)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate, debug, review, and explain UIFlow2 MicroPython code for M5Stack devices. It helps select documented APIs, imports, constructors, UI patterns, hardware drivers, and verification steps from bundled UIFlow2 references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated hardware code can activate sensitive device behaviors involving biometrics, microphones, location, USB keyboard or mouse mode, motors, relays, QR scanning, or network credentials.

Mitigation: Review generated code before running it and add explicit user consent, visible indicators, safety interlocks, secure storage, credential replacement, and encrypted transport where supported.

Risk: Bundled examples may be adapted into production without enough privacy or safety controls.

Mitigation: Treat examples as structural references and add production-specific safety, privacy, and hardware validation before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuyun2000/skills/uiflow2-coder)
- [UIFlow2 get-started overview](artifact/docs/get-started/_overview.md)
- [M5UI overview](artifact/docs/m5ui/_overview.md)
- [Widgets overview](artifact/docs/widgets/_overview.md)
- [Curated UIFlow2 examples](artifact/references/complex-examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with MicroPython code blocks, concise explanations, document paths consulted, and hardware verification steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are grounded in bundled UIFlow2 documentation and may include device-specific assumptions when hardware details are missing.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
