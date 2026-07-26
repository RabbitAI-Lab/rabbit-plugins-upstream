## Description: <br>
Guides agents through S-curve technology adoption diagnosis to locate market phase, estimate saturation, and recommend strategy shifts across adopter categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, strategists, and operators use this skill when an agent needs to analyze stalled growth, market saturation timing, chasm risk, or adoption strategy for an innovation spreading through a population. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce misleading strategy guidance if users ask it to diagnose adoption without time-indexed adoption data or an estimated addressable population. <br>
Mitigation: Require the agent to surface missing data, avoid curve-fitting claims when evidence is insufficient, and frame projections as uncertain. <br>
Risk: Business recommendations may not fit markets where adoption is mature, mandated, or capped by external constraints. <br>
Mitigation: Apply the documented fit checks before analysis and decline or qualify the S-curve framing when diffusion dynamics do not apply. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deciqai/skills/s-curve-technology-adoption) <br>
- [deciqAI Skill Page](https://www.deciqai.com/c/s-curve-technology-adoption) <br>
- [Machine-Readable Skill Metadata](https://www.deciqai.com/s/s-curve-technology-adoption.json) <br>
- [Primary Sources](references/sources.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Structured Markdown diagnosis with adoption data, current phase evidence, saturation ceiling, trajectory projection, strategy audit, chasm plan, and second-curve plan.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires time-indexed adoption data or explicit uncertainty when data is insufficient.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
