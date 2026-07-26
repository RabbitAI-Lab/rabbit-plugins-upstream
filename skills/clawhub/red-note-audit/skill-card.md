## Description: <br>
Red Note Audit reviews Xiaohongshu (RED) note content for policy compliance, shadowban risk, and optimization opportunities using an external WSD Social API that requires an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wsd-mj](https://clawhub.ai/user/wsd-mj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and developers use this skill to submit Xiaohongshu (RED) note text for compliance checks, shadowban risk assessment, and visibility optimization suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted RED note text and the API key are sent to ai.wsdsocial.com. <br>
Mitigation: Avoid submitting confidential drafts, personal data, or client material unless the provider's data handling terms are acceptable. <br>
Risk: The skill requires a WSD Social API key. <br>
Mitigation: Store the key in WSD_API_KEY and avoid hard-coding it in prompts, files, shell history, or logs. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/WSD-MJ/red-note-audit) <br>
- [ClawHub skill page](https://clawhub.ai/wsd-mj/skills/red-note-audit) <br>
- [WSD Social API key portal](https://ai.wsdsocial.com/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance] <br>
**Output Format:** [Text or structured API response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WSD_API_KEY and sends the submitted RED note content to ai.wsdsocial.com.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
