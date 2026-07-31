## Description: <br>
Analyzes full-body pet image or video inputs to estimate breed or body type and fur density, then returns a non-medical drying temperature and time curve for pet-care equipment or grooming workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, grooming teams, and smart pet-care device developers use this skill to analyze pet media and produce non-medical drying temperature guidance, structured reports, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends pet images, videos, URLs, and report-history requests to remote services, and server evidence reports local identity and authentication token persistence. <br>
Mitigation: Review the publisher and remote-processing model before installation; use only media and URLs appropriate for cloud processing, and clear local identity or token state when no longer needed. <br>
Risk: Drying-temperature recommendations may be inaccurate or unsuitable for an individual animal. <br>
Mitigation: Treat outputs as non-medical care guidance, keep temperatures within device and animal safety limits, and have a human review the recommendation before applying it to equipment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-adaptive-pet-drying-temperature-analysis) <br>
- [Pet drying recommendation API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis output with recommended drying temperatures, durations, warnings, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can analyze a local pet media file or network URL, select pet type, list cloud report history, and optionally save output to a file.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
