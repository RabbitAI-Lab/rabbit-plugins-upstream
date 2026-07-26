## Description: <br>
Stormglass helps an agent retrieve forecast weather, hourly tide sea-level data, and high or low tide extremes for a single coordinate through an OOMOL-connected Stormglass account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when they want an agent to answer Stormglass weather or tide questions by running the OOMOL oo CLI connector instead of calling Stormglass directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First-time use can require installing the oo CLI and creating a persistent OOMOL and Stormglass connection. <br>
Mitigation: Install and connect only when needed, and clarify ambiguous Stormglass requests before running connector commands. <br>


## Reference(s): <br>
- [Stormglass homepage](https://stormglass.io/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and connector JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Stormglass connector actions return JSON data with an execution id; first-time setup may require oo CLI authentication and a Stormglass connection.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
