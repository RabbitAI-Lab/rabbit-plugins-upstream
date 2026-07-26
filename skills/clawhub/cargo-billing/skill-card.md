## Description: <br>
Pull usage metrics, check subscription status, view invoices, and manage credits using the Cargo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cargo workspace administrators and operators use this skill to inspect billing usage, subscription state, invoices, credit balances, and billing portal access through the Cargo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Billing, invoice, card-on-file, and portal-session commands can reveal sensitive workspace billing details. <br>
Mitigation: Use trusted Cargo CLI credentials, limit use to intended admin workflows, and review commands before running them. <br>
Risk: Sample workflow-run commands used for cost estimates can consume credits. <br>
Mitigation: Run only small samples, check available credits before larger batches, and monitor usage during execution. <br>


## Reference(s): <br>
- [Cargo Billing skill page](https://clawhub.ai/cargo-ai/skills/cargo-billing) <br>
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills) <br>
- [Response shapes](references/response-shapes.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Usage metrics examples](references/examples/usage-metrics.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the Cargo CLI and admin-level Cargo billing access.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
