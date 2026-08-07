## Description: <br>
Retrieves patent claims data from Zhihuiya (PatSnap) by patent ID or publication number and helps agents present claim text, claim counts, and family-substitution notices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, IP professionals, patent analysts, and R&D teams use this skill to retrieve and present patent claim text and claim counts for one or more patent IDs or publication numbers. It is suited to claims lookup and display, not legal interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers, claim queries, API credentials, and session metadata may be sent to LinkFox or Zhihuiya services. <br>
Mitigation: Use the skill only when the user accepts that data sharing, and keep API credentials scoped to trusted use. <br>
Risk: The network gateway can be overridden with LINKFOX_TOOL_GATEWAY, which could route authenticated requests to an unintended endpoint. <br>
Mitigation: Set LINKFOX_TOOL_GATEWAY only to a trusted endpoint or leave it unset to use the default LinkFox gateway. <br>
Risk: Full patent-claims responses and cache data are written under local linkfox directories and may include sensitive patent data. <br>
Mitigation: Review where response files are stored and delete cached or saved data when it is no longer needed. <br>
Risk: Queries can consume paid credits, and onboarding or feedback flows may make additional network requests. <br>
Mitigation: Ask for explicit user consent before paid calls, onboarding-skill installation, or feedback submission. <br>


## Reference(s): <br>
- [Zhihuiya Claims API Reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and saved JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script saves full API responses locally, prints small responses inline, summarizes larger responses, and uses a 24-hour local cache.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
