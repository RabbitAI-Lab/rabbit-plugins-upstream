## Description:

OnePageCRM helps agents read, create, and update CRM contacts and deals through the OOMOL OnePageCRM connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate OnePageCRM from an agent, including listing and retrieving contacts or deals and creating new CRM records after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts when the oo CLI is missing.

Mitigation: Review the skill before installing; install oo through a verified, version-pinned, or package-manager path, and do not let an agent automatically run remote installer commands.

Risk: Write actions can create contacts or deals and change OnePageCRM data.

Mitigation: Confirm the exact payload and expected effect with the user before running any action marked as write.

## Reference(s):

- [OnePageCRM skill page](https://clawhub.ai/oomol/skills/oo-one-page-crm)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OnePageCRM homepage](https://www.onepagecrm.com/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return CRM data and connector execution metadata from oo CLI actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
