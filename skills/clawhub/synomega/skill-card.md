## Description: <br>
Retrosynthesis helper for legitimate cheminformatics tasks using the synomega Python package, including single-step reactant prediction, multi-step route planning, and synthesizability scoring for target molecules provided as SMILES. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbc0315](https://clawhub.ai/user/zbc0315) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, chemistry researchers, and cheminformatics users can use this skill to ask an agent for candidate disconnections, synthesis route plans, or makeability scores for specific target molecules. The host safety policy remains responsible for deciding whether requests involving hazardous, controlled, or dual-use compounds are allowed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First use may download a few hundred MB of model and stock data into a local cache. <br>
Mitigation: Prefetch the data, set a controlled cache location, or use local model and stock files in bandwidth-limited, air-gapped, privacy-sensitive, or reproducibility-critical environments. <br>
Risk: Retrosynthesis can provide operational route assistance for hazardous, controlled, or otherwise dual-use compounds. <br>
Mitigation: Apply the host safety policy before planning routes or providing actionable assistance for high-risk targets, and decline or escalate requests that appear unsafe. <br>


## Reference(s): <br>
- [Synomega package on PyPI](https://pypi.org/project/synomega/) <br>
- [SynOmega Skill on ClawHub](https://clawhub.ai/zbc0315/skills/synomega) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-producing helper commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Helper commands can output JSON for single-step predictions, route plans, and synthesizability scores.] <br>

## Skill Version(s): <br>
1.4.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
