## Description: <br>
Synomega Skill helps agents use the local synomega Python package to predict single-step reactants, plan multi-step retrosynthesis routes, and compute SynScore for target molecules provided as SMILES. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbc0315](https://clawhub.ai/user/zbc0315) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, cheminformatics practitioners, and chemistry users use this skill to ask an agent for legitimate retrosynthesis support: candidate reactants, route planning to purchasable building blocks, or makeability scoring for a molecule. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First use downloads model and stock files, which may be unsuitable for controlled, offline, privacy-sensitive, or reproducibility-critical environments. <br>
Mitigation: Prefetch or provide local model and stock files, pin trusted sources, configure cache and mirror settings, and treat network downloads as explicit opt-in. <br>
Risk: Retrosynthesis route planning can provide operational assistance for hazardous, controlled, or otherwise regulated compounds. <br>
Mitigation: Apply the host safety policy and require additional review before producing synthesis routes for high-risk targets. <br>


## Reference(s): <br>
- [SynOmega package on PyPI](https://pypi.org/project/synomega/) <br>
- [SynOmega toolkit source](https://github.com/zbc0315/synomega) <br>
- [ClawHub skill page](https://clawhub.ai/zbc0315/skills/synomega) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell and Python examples; the helper script prints JSON for score, plan, and single-step operations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [First use may download model and stock files unless local paths are configured.] <br>

## Skill Version(s): <br>
1.4.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
