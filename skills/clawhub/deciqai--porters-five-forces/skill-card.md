## Description: <br>
Guides agents through a structured Porter's Five Forces analysis for industry attractiveness, profitability, and competitive strategy decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business strategists, operators, investors, and agents use this skill to define an industry boundary, score the five competitive forces, identify the binding force, and propose a targeted strategic response. It is intended for established industries or sectors with enough evidence to validate the analysis against profitability and market data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Included industry examples may be mistaken for current market truth. <br>
Mitigation: Treat examples as analysis templates and re-verify market structure, profitability, technology, and regulatory data before making decisions. <br>
Risk: The framework can be misapplied to platforms, very new markets, dynamic disruptions, or firm-level questions. <br>
Mitigation: Check fit before use and switch frameworks when buyer/supplier roles are ambiguous, industry structure is unstable, or the question is about firm-specific advantage. <br>
Risk: Force scores can become subjective if the agent lacks evidence. <br>
Mitigation: Require a defined industry boundary, named drivers for each score, one binding force, and validation against external profitability or market data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/porters-five-forces) <br>
- [Sources - porters-five-forces](references/sources.md) <br>
- [Porter 2008 HBR update](https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy) <br>
- [McGahan and Porter 1997 empirical study](https://doi.org/10.1002/(SICI)1097-0266(199707)18:1+<15::AID-SMJ916>3.3.CO;2-T) <br>
- [Damodaran industry-level returns dataset](http://pages.stern.nyu.edu/~adamodar/) <br>
- [Stanford AI Index Report](https://aiindex.stanford.edu/report/) <br>
- [NVIDIA investor relations and financial results](https://investor.nvidia.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown five-forces analysis with a scoring table, binding-force finding, strategic response, and validation note] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask stepwise clarification questions in coach mode before producing the final analysis.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
