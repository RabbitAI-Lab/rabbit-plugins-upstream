## Description: <br>
Analyzes fixed-camera reptile enclosure videos to estimate basking, hiding, cool-zone movement, dwell time, activity rhythm, and thermal preference signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze reptile enclosure videos or video URLs, produce structured thermal-zone utilization reports, and receive non-diagnostic husbandry guidance about basking, hiding, movement, and activity rhythm. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends reptile enclosure videos or video URLs to the Life Emergence cloud service for analysis. <br>
Mitigation: Use only footage that is appropriate for cloud processing, obtain required authorization for shared or farm cameras, and avoid sensitive media. <br>
Risk: The skill may create or reuse a cloud-linked identity and store authentication tokens locally. <br>
Mitigation: Install only in workspaces where local token storage is acceptable, and review deletion procedures for local data, tokens, and cloud reports before use. <br>
Risk: Behavior analysis can be mistaken for veterinary diagnosis or treatment advice. <br>
Mitigation: Treat outputs as husbandry and welfare signals only; confirm health concerns with direct observation and a qualified reptile veterinarian. <br>


## Reference(s): <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with recommended actions and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include thermal preference labels, zone dwell ratios, transition counts, alert level, recommended actions, and historical report links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
