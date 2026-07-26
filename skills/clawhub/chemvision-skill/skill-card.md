## Description: <br>
Chemvision helps agents answer chemistry questions by querying PubChem and OPSIN for compound data, safety information, molecular structures, and reaction context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[panda-lsy](https://clawhub.ai/user/panda-lsy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and chemistry-focused agent users can use this skill to look up compounds, inspect SMILES strings, retrieve GHS safety information, render molecular structures or equations, and gather data that supports reaction explanations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports inconsistent privacy and runtime disclosures, including possible external queries for chemical names, SMILES strings, reaction inputs, or safety lookups. <br>
Mitigation: Avoid confidential research compounds unless the publisher clarifies network behavior or provides an offline mode, and review the service behavior before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/panda-lsy/skills/chemvision-skill) <br>
- [Source repository](https://github.com/panda-lsy/chemvision-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands, API request examples, and links to rendered structure or equation images] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to start a local service, call local HTTP tool endpoints, translate Chinese chemical names to English for tool calls, and return generated molecular structure or equation images.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata; artifact metadata reports skill_version 3.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
