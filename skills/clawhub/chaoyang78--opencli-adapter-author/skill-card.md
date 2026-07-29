## Description: <br>
Guides developers through writing or extending OpenCLI browser adapters, from site reconnaissance and data-source strategy through field decoding, adapter implementation, and verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaoyang78](https://clawhub.ai/user/chaoyang78) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build new OpenCLI adapters or add commands to existing site adapters. It helps them choose a data-fetching strategy, decode fields, design output columns, write adapter code, verify behavior, and preserve site knowledge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide inspection of browser session data and authenticated network responses during adapter development. <br>
Mitigation: Use it only on sites and accounts the operator is authorized to test, prefer test or low-risk browser profiles, and avoid real sensitive sessions when possible. <br>
Risk: Captured fixtures, traces, logs, or site-memory notes may contain cookies, tokens, account data, or user-specific response content. <br>
Mitigation: Redact cookies, tokens, identifiers, and user data before saving or sharing artifacts, fixtures, traces, or logs. <br>
Risk: Adapter workflows may replay authenticated or mutating requests if the operator chooses an unsafe target or command. <br>
Mitigation: Do not replay mutating requests unless the operator controls the account and accepts the impact; keep implementation focused on legitimate reuse of data the page already obtained. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chaoyang78/skills/opencli-adapter-author) <br>
- [Adapter Template](references/adapter-template.md) <br>
- [API Discovery](references/api-discovery.md) <br>
- [Coverage Matrix](references/coverage-matrix.md) <br>
- [Field Conventions](references/field-conventions.md) <br>
- [Field Decode Playbook](references/field-decode-playbook.md) <br>
- [JSDOM Fixture Pattern](references/jsdom-fixture-pattern.md) <br>
- [Output Design](references/output-design.md) <br>
- [Site Memory](references/site-memory.md) <br>
- [Site Recon](references/site-recon.md) <br>
- [Strategy Selection](references/strategy-selection.md) <br>
- [Success-Rate Pitfalls](references/success-rate-pitfalls.md) <br>
- [Typed Error Conventions](references/typed-errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with checklists, code snippets, shell commands, and adapter configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent output may include strategy notes, adapter source edits, verification commands, fixtures, and site-memory updates.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
