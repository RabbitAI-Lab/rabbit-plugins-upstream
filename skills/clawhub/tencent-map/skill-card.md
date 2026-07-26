## Description: <br>
Tencent Map provides Tencent Maps WebService API guidance and a zero-dependency Python CLI for geocoding, POI search, routing, IP location, and WeChat Mini Program LBS integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run Tencent Maps WebService lookups, troubleshoot WeChat Mini Program map integrations, and avoid coordinate-order mistakes when working with GCJ-02 locations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generic API helper can expose the Tencent Maps API key to an unintended host if it is used with a crafted path. <br>
Mitigation: Use only trusted Tencent Maps /ws/... paths with the call command and avoid high-value or broadly privileged Tencent Maps keys until path validation or host enforcement is in place. <br>


## Reference(s): <br>
- [ClawHub Tencent Map Skill](https://clawhub.ai/zhangifonly/skills/tencent-map) <br>
- [Tencent Maps API Host](https://apis.map.qq.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses from the helper CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses QQMAP_KEY for Tencent Maps WebService API calls; no server-resolved provenance is available for this release.] <br>

## Skill Version(s): <br>
2.0.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
