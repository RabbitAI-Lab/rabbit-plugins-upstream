## Description: <br>
HERE connector access for searching and reading location data through the OOMOL oo CLI rather than direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to access HERE search, autocomplete, autosuggest, geocoding, reverse geocoding, and lookup workflows through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use configured service accounts and local helper scripts for HERE operational workflows. <br>
Mitigation: Install only when that access is intended and use scoped API tokens for the connected account. <br>
Risk: Incorrect action payloads could produce unintended HERE queries or results. <br>
Mitigation: Inspect the live connector schema before building each payload and review any action that changes state before execution. <br>


## Reference(s): <br>
- [HERE homepage](https://www.here.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub HERE skill page](https://clawhub.ai/oomol/skills/oo-here) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
