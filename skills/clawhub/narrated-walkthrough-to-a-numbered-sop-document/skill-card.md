## Description: <br>
Narrated Walkthrough to a Numbered SOP Document turns spoken job walkthroughs into written, numbered standard operating procedures for maintenance, facilities, field service, manufacturing, lab, franchise, and owner-operator teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators, documentation owners, and operations teams use this skill to turn Plaud-recorded narrated work walkthroughs into editable numbered SOP documents. The workflow helps preserve tools, safety notes, warnings, skipped recordings, and unresolved ambiguities for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plaud transcript content and extracted procedure details may be sent to and stored in connected Google Docs and Google Sheets accounts. <br>
Mitigation: Use only approved connected accounts and avoid confidential, regulated, or highly sensitive recordings unless those services are approved for that data. <br>
Risk: A narrated walkthrough may leave procedural details ambiguous or unsuitable for direct operational use. <br>
Mitigation: Keep ambiguous points in a human-review section and review the SOP before relying on it for training, maintenance, or operations. <br>
Risk: Recording timestamp handling can select or skip the wrong Plaud recording if local time and UTC fields are compared directly. <br>
Mitigation: Resolve the user's timezone, convert Plaud timestamps before filtering, and review the generated summary and processing log. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/narrated-walkthrough-to-a-numbered-sop-document) <br>
- [AgentPMT workflow page](https://www.agentpmt.com/agent-workflow-skills/narrated-walkthrough-to-a-numbered-sop-document) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [Plaud connector](https://clawhub.ai/agentpmt/plaud) <br>
- [Google Docs Connector](https://clawhub.ai/agentpmt/google-docs-connector) <br>
- [Google Sheets](https://clawhub.ai/agentpmt/google-sheets) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, API calls] <br>
**Output Format:** [Markdown workflow guidance with JSON tool-call examples; generated SOP content is written to Google Docs and run status is logged to Google Sheets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow preserves numbered steps, safety notes, tools, warnings, skipped-recording reasons, and a human-review section for ambiguities.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
