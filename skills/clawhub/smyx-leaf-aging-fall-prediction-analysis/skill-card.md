## Description: <br>
This skill analyzes fixed-angle indoor plant image or video sequences to detect leaf aging signals and predict leaf-fall risk windows over the next 3-7 days. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, plant-care operators, greenhouse teams, and developers use this skill to analyze indoor plant media, identify aging indicators, estimate leaf-fall timing, and receive directional care guidance. It can also query prior cloud reports associated with the active platform identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant photos, videos, or media URLs may be sent to a remote cloud service for analysis. <br>
Mitigation: Use only media approved for remote processing and review data-sensitivity requirements before installation. <br>
Risk: The skill may create or reuse an internal account and persist returned service tokens locally. <br>
Mitigation: Run it in an isolated workspace or account and review token persistence and identity binding before deployment. <br>
Risk: History lookup may list prior cloud reports associated with the active platform identity. <br>
Mitigation: Confirm identity separation and report-access expectations before enabling historical report queries. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis report with optional saved file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and historical report tables from the remote service.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
