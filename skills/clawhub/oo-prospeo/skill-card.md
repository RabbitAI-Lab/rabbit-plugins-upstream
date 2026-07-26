## Description: <br>
Prospeo lets agents search and enrich people or company data through the OOMOL-managed Prospeo connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Prospeo company and people search, enrichment, search suggestion, and account information actions through an OOMOL-connected Prospeo account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search and enrichment payloads may include sensitive people or company data and are sent to the Prospeo connector. <br>
Mitigation: Confirm the lookup is appropriate, minimize submitted fields, and avoid sending sensitive data unless the user has authorization. <br>
Risk: Prospeo or OOMOL account credits may be consumed by searches and enrichment requests. <br>
Mitigation: Use targeted queries, check account information when needed, and stop on billing or insufficient-credit errors. <br>
Risk: The skill runs shell commands through the oo CLI against a connected Prospeo account. <br>
Mitigation: Fetch the live connector schema before building payloads and confirm any action that is marked write or destructive before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-prospeo) <br>
- [Prospeo homepage](https://prospeo.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live Prospeo connector schemas before constructing payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
