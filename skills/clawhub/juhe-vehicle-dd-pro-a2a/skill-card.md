## Description: <br>
Provides a paid vehicle due-diligence workflow that uses a VIN, vehicle type, and accident or illegal-modification status to produce a pre-purchase report covering configuration data, registration fields, ownership transfer history, and inspection timing estimates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill when a buyer, lender, insurer, or vehicle reviewer needs a paid pre-purchase quick check for a specific VIN. It is intended for due-diligence scenarios that need configuration details, registration fields, transfer history, and a structured Markdown report rather than only configuration lookup or only ownership transfer lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends a VIN, vehicle type, and accident or illegal-modification status to a third-party provider for a paid lookup. <br>
Mitigation: Require clear user consent before payment and send only the documented fields needed for the lookup. <br>
Risk: Returned registration-related data may include a license plate. <br>
Mitigation: Mask license plates in reports, follow-up answers, and logs, and avoid local persistent storage of full VIN or plate values. <br>
Risk: Vehicle reports can be overread as definitive valuation, accident, theft, lien, insurance, or purchase advice. <br>
Mitigation: Present the report as a public-information quick check, keep price fields as reference values only, and avoid deterministic buy-or-do-not-buy conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vehicle-dd-pro-a2a) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>
- [README.md](artifact/README.md) <br>
- [PRODUCT.md](artifact/PRODUCT.md) <br>
- [OUT_FORMAT.md](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with structured sections and inline shell command examples for the payment-backed query workflow] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports must use returned provider data only, mask license plates, avoid raw JSON in user-facing output, and avoid buy-or-do-not-buy conclusions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
