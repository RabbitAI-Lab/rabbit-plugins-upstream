## Description: <br>
Operate Waterfall through an OOMOL-connected account to verify emails, check job changes, review usage, and launch or retrieve contact and company enrichment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run Waterfall account, enrichment, email verification, and job-change workflows through the oo CLI with an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Enrichment launch actions can start work under the connected Waterfall account and may incur account usage or cost. <br>
Mitigation: Require explicit user confirmation of the action, payload, target account context, and expected effect before running launch_contact_enrichment or launch_company_enrichment. <br>
Risk: The setup path includes remote oo CLI installer commands. <br>
Mitigation: Install only when the oo CLI is missing, review the installer before execution, and proceed only when OOMOL is trusted for the deployment. <br>
Risk: Incorrect payloads can produce unintended enrichment or verification requests. <br>
Mitigation: Fetch the live action schema with oo connector schema before constructing payloads and validate JSON inputs against that schema. <br>


## Reference(s): <br>
- [ClawHub Waterfall skill](https://clawhub.ai/oomol/skills/oo-waterfall) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Waterfall homepage](https://www.waterfall.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands should inspect live connector schemas before building payloads; enrichment launch actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
