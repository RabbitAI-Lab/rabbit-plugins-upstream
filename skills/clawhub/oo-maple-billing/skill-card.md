## Description:

Operate Measure through OOMOL's maple_billing connector for reading, creating, and updating Measure data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Measure through an OOMOL-connected account, including retrieving customers, products, pricing, subscriptions, and checkout sessions. With confirmation, it can also create checkout sessions and customers or update customer records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI, which can be risky if run without review.

Mitigation: Review installer commands before use, prefer a verified or package-manager installation path where available, and avoid running remote scripts in an elevated shell.

Risk: Measure actions tagged as write can create checkout sessions or customers and update customer records.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [Measure homepage](https://getmeasure.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-maple-billing)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; responses may include JSON data and execution metadata from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
