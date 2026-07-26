## Description: <br>
Firstbase connector skill for searching and reading Firstbase account data through OOMOL's oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators with an OOMOL-connected Firstbase account use this skill to inspect Firstbase catalog SKUs, inventory items, brands, categories, and organization inventory without handling raw Firstbase API tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Firstbase account data through an OOMOL-connected account. <br>
Mitigation: Install and use it only when the OOMOL and Firstbase connection is intentional and appropriate for the requested account data. <br>
Risk: Future connector actions marked write or destructive could change or remove Firstbase data. <br>
Mitigation: Require explicit user confirmation of the exact payload, target, and effect before running any write or destructive action. <br>


## Reference(s): <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Firstbase homepage](https://www.firstbase.com) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before running Firstbase actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
