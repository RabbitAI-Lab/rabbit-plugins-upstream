## Description: <br>
Analyzes fixed-camera reptile enclosure videos to report basking and hiding dwell time, zone transitions, thermal preference, activity rhythm, and abnormal thermoregulation alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, reptile keepers, breeders, and smart-enclosure app integrations use this skill to analyze enclosure video, identify thermoregulation patterns, and generate daily zone-utilization reports with non-diagnostic recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reptile videos, video URLs, and report requests may be sent to the publisher's cloud service, and the security evidence notes local identity, external account session, and cached token behavior. <br>
Mitigation: Use only footage and URLs appropriate for the publisher to process, avoid private signed URLs or sensitive camera footage, and review account and retention behavior before deployment. <br>
Risk: Behavior reports and alerts could be mistaken for veterinary diagnosis or automatic device-control decisions. <br>
Mitigation: Treat outputs as behavior analysis and husbandry guidance only; confirm health concerns with a qualified reptile veterinarian and require user confirmation for any equipment changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown summaries and JSON analysis reports with optional shell command invocations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links, historical report tables, alert levels, and non-diagnostic husbandry recommendations.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
