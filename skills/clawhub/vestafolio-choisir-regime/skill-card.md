## Description:

Determines which French business legal forms an entrepreneur is eligible for and recommends a structure using Vestafolio's simulator API after collecting profile details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business advisors use this skill to orient entrepreneurs choosing a French business legal form such as micro-entreprise, EI, EURL, SASU, SARL, SAS, SELARL, or SELAS. The skill asks for activity, projected turnover, existing-business status, liability needs, partners, and unemployment-insurance preferences before returning qualitative guidance.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: Business-profile and optional household financial details may be sent to Vestafolio.

Mitigation: Disclose the external API call before use and send optional family or household-income fields only when the user knowingly provides and approves them.

Risk: French legal-structure thresholds and eligibility rules may change over time.

Mitigation: Present outputs as qualitative orientation based on the simulator result, state assumptions and limits, and direct the user to the Vestafolio simulator or qualified legal advice for confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-choisir-regime)
- [Vestafolio choisir-regime simulator](https://www.vestafolio.com/simulateurs/choisir-regime)
- [Vestafolio choisir-regime API endpoint](https://www.vestafolio.com/api/tools/v1/choisir-regime)

## Skill Output:

**Output Type(s):** [Guidance, Text, API Calls]

**Output Format:** [Markdown or plain text responses grounded in JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responds in French when the user writes in French; qualitative orientation only, with no tax or cotisation calculations.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter declares 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
