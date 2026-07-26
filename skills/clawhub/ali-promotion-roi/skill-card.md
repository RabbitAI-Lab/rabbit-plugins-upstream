## Description: <br>
Analyzes Alibaba International promotion ROI by comparing CNY promotion spend with completed-order counts and USD revenue from pre-loaded MySQL data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cloudcode-hans](https://clawhub.ai/user/cloudcode-hans) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and ecommerce analysts use this skill to generate Alibaba International promotion ROI reports, compare standard and sitewide promotion performance, and investigate discrepancies between platform-reported orders and completed orders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads business order and promotion data from configured MySQL tables and automatically approves sql-linker-cli credential access. <br>
Mitigation: Install it only where that credential gate approval is acceptable and confirm access to alibaba_intl_orders and alibaba_intl_promotion_daily is appropriate. <br>
Risk: Full reports can read all available months of order and promotion data. <br>
Mitigation: Use month filters for narrower reports when reviewing, exporting, or sharing results. <br>


## Reference(s): <br>
- [Metrics definitions](references/metrics.md) <br>
- [Database schema](references/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and optional JSON report output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI options support month filtering, exchange-rate override, by-type reports, by-date reports, and JSON output.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
