## Description: <br>
检查大群空间 (LegionSpace, package: com.tongfudun.legion) 在 Apple App Store, Tencent MyApp, Xiaomi, vivo, Honor, Huawei AppGallery, and OPPO 应用商店的最新版本号. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, release managers, and operations teams use this skill to query and compare LegionSpace app version availability across major Chinese app stores and the Apple App Store. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may automatically install Python packages, Playwright, and Chromium during normal use. <br>
Mitigation: Review before installing and run in an isolated or approved environment where dependency and browser installation is acceptable. <br>
Risk: The skill bypasses configured proxy settings for outbound app-store requests. <br>
Mitigation: Use only on machines and networks where direct outbound requests to the referenced app-store endpoints are permitted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/legionspace-version) <br>
- [Publisher profile](https://clawhub.ai/user/legionspace-hackathon) <br>
- [Apple iTunes Lookup API query](https://itunes.apple.com/cn/lookup?bundleId=com.tongfudun.legion) <br>
- [Tencent MyApp listing](https://sj.qq.com/appdetail/com.tongfudun.legion) <br>
- [Xiaomi app listing](https://app.mi.com/details?id=com.tongfudun.legion) <br>
- [vivo app listing](https://h5.appstore.vivo.com.cn/#/appinfo?appId=com.tongfudun.legion) <br>
- [Honor app listing](https://app.honor.com/appDetail/com.tongfudun.legion) <br>
- [Huawei AppGallery listing](https://appgallery.huawei.com/app/C109776267) <br>
- [OPPO app listing](https://store.oppo.com/app/com.tongfudun.legion) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, guidance] <br>
**Output Format:** [Console text and a plain-text version report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes scripts/LegionSpace_versions.txt with queried store versions and error or N/A statuses.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
