## Description: <br>
Real-time detection of flames and smoke in video and image scenes. Suitable for fire early warning in industrial parks, forests, warehouses, and other locations. | 火情烟雾检测技能，实时检测视频/图片场景中的火焰、烟雾，适用于工业园区、森林、仓库等场所火情预警 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, operators, and developers use this skill to analyze images, videos, or media URLs for flames and smoke, receive structured fire-warning results, and retrieve cloud-stored historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded media or media URLs may be sent to the provider's remote service for analysis. <br>
Mitigation: Use only media that is acceptable to share with the provider and confirm remote service retention and handling before deployment. <br>
Risk: The skill may create or bind an internal user identity, store local identity or token data, and query cloud report history. <br>
Mitigation: Review account and local token behavior before installation, restrict workspace access, and avoid sensitive surveillance footage unless this behavior is acceptable. <br>
Risk: Fire and smoke detection results are warning-support outputs and may be incomplete or incorrect. <br>
Mitigation: Use outputs as an early-warning aid and require professional or operational confirmation for fire response decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown or JSON analysis reports with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report export links and history report lists; supports jpg/jpeg/png/mp4/avi/mov inputs up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.15 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
