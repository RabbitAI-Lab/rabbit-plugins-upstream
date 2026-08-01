## Description: <br>
Analyzes fixed-camera reptile enclosure videos to report basking, hiding, cool-zone, and transition-zone use, movement frequency, activity rhythm, thermal preference labels, reminders, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, enclosure operators, and developers use this skill to analyze enclosure videos or URLs for thermal-zone utilization, activity rhythm, abnormal immobility, and husbandry-oriented recommendations. It is intended to support welfare monitoring and environment adjustment decisions, not veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends enclosure videos or URLs to the publisher's cloud service for analysis. <br>
Mitigation: Use only footage the user is comfortable sharing with the publisher service, avoid sensitive home footage, and confirm authorization before processing shared or farm camera feeds. <br>
Risk: The security evidence says the skill can silently create or reuse local identities and store account tokens and report-history state in the workspace data directory. <br>
Mitigation: Run it in an isolated workspace, restrict access to local state files, and clear or rotate local identity state before handing the workspace to another user. <br>
Risk: The security evidence says historical cloud reports can be queried with limited user control. <br>
Mitigation: Use separate identities for separate users or enclosures and review report access expectations before using the history-list feature in shared environments. <br>
Risk: Behavior reports may be mistaken for veterinary diagnosis or direct device-control instructions. <br>
Mitigation: Treat outputs as husbandry guidance, require user confirmation for any heating or lighting changes, and consult a reptile veterinarian for health concerns. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with command examples and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report output to a user-specified file; historical report queries are presented as Markdown tables.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter lists 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
