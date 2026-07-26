## Description: <br>
Retrieves translated patent claim text from the Zhihuiya (PatSnap) patent database in Chinese, English, or Japanese for one patent at a time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and patent analysts use this skill to retrieve translated claim text for a known patent ID or publication number. It is suited to single-patent claim review, claim translation, and family-patent fallback when the original claims are unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers, API credentials, and session metadata are sent to LinkFox services. <br>
Mitigation: Use only when those disclosures are acceptable, and avoid confidential patent work unless the deployment has appropriate data-handling controls. <br>
Risk: Full API responses are cached or written locally in the linkfox session data directory. <br>
Mitigation: Review, protect, and clean up saved linkfox data according to the workspace's retention and access-control requirements. <br>
Risk: The skill can report feedback automatically without a clear consent step. <br>
Mitigation: Review feedback behavior before deployment and disable or avoid feedback reporting where user consent or confidentiality requirements apply. <br>


## Reference(s): <br>
- [API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-claim-data-translated) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes complete API responses under a local linkfox session data directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
