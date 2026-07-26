## Description: <br>
Search PatSnap's TRIZ case library through its hosted MCP endpoint using plain HTTP, including keyword, technical-contradiction, SVOP, efficacy, Oxford-effect, patent-office, legal-status, applicant, and IPC/CPC criteria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwt1995](https://clawhub.ai/user/wwt1995) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical teams use this skill to search for analogous TRIZ solution cases, cross-domain mechanisms, invention principles, scientific effects, and prior solution patterns for a technical problem. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search criteria and technical problem details are sent to PatSnap's hosted endpoint. <br>
Mitigation: Redact sensitive information and avoid trade secrets, NDA-protected details, personal information, unreleased proprietary technology, and export-controlled content unless the organization has approved that data flow. <br>
Risk: Analogous case-search results may be mistaken for proof of feasibility, freedom to operate, or legal clearance. <br>
Mitigation: Use retrieved cases as inspiration only and require separate engineering validation, patent review, and legal review before relying on the results. <br>


## Reference(s): <br>
- [Solution Case Finder on ClawHub](https://clawhub.ai/wwt1995/skills/solution-case-finder) <br>
- [PatSnap TRIZ Case Library MCP endpoint](https://ai-fabric.patsnap.com/mcp/patsnap-triz-case-library?APP_ID=Patsnap) <br>
- [Eureka RD](https://eureka.patsnap.com/rd/#/agentic?type=triz&start_from=hub) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with bash examples and JSON tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results should include case identifiers, problem and solution mechanisms, TRIZ principles or effects, transferable insights, and limitations when available.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
