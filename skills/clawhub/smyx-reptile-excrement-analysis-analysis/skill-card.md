## Description: <br>
This skill analyzes reptile enclosure images or video frames to identify urate size and feces morphology, then returns structured health prompts and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, farms, and developers can use this skill to evaluate camera images or video frames of reptile excrement, track urate and feces signals, and retrieve historical reports. It is intended to support visual health monitoring workflows, not veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media and identity-bearing requests may be sent to lifeemergence.com services. <br>
Mitigation: Use only with media and report data appropriate for those external services, and avoid sensitive environments unless that data flow has been reviewed. <br>
Risk: The skill may automatically create or reuse a local/cloud identity and store tokens locally. <br>
Mitigation: Run in an isolated workspace where practical, and review or remove stored workspace data and tokens before and after use. <br>
Risk: Visual health prompts could be mistaken for veterinary diagnosis. <br>
Mitigation: Treat outputs as visual monitoring support and have abnormal findings reviewed by a qualified reptile veterinarian. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-excrement-analysis-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May send media and identity-bearing requests to external lifeemergence.com services; historical report listings are returned from cloud APIs.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
