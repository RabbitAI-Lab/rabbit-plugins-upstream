## Description: <br>
Checks the latest version numbers for LegionSpace (package com.tongfudun.legion) across Apple App Store, Tencent MyApp, Xiaomi, vivo, Honor, Huawei AppGallery, and OPPO. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, release teams, and support teams use this skill to query and compare published LegionSpace versions across major Chinese app stores and save a plain-text report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts several public app-store sites while checking version information. <br>
Mitigation: Run it only in environments where those outbound requests are approved, and review the contacted domains before deployment. <br>
Risk: The launcher may install Python packages and Playwright Chromium dependencies before running the checker. <br>
Mitigation: Prefer preinstalling reviewed, pinned dependencies through a trusted setup process in managed environments. <br>
Risk: The skill bypasses configured proxies while making network requests. <br>
Mitigation: Remove or review the proxy override before use in corporate or managed networks. <br>
Risk: The skill writes a version report into the skill scripts directory. <br>
Mitigation: Run it from an approved workspace and review the output path before execution. <br>


## Reference(s): <br>
- [Apple App Store lookup endpoint](https://itunes.apple.com/cn/lookup?bundleId=com.tongfudun.legion) <br>
- [Tencent MyApp app detail](https://sj.qq.com/appdetail/com.tongfudun.legion) <br>
- [Xiaomi app detail](https://app.mi.com/details?id=com.tongfudun.legion) <br>
- [vivo app detail](https://h5.appstore.vivo.com.cn/#/appinfo?appId=com.tongfudun.legion) <br>
- [Honor app detail](https://app.honor.com/appDetail/com.tongfudun.legion) <br>
- [Huawei AppGallery app detail](https://appgallery.huawei.com/app/C109776267) <br>
- [OPPO app detail](https://store.oppo.com/app/com.tongfudun.legion) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, guidance] <br>
**Output Format:** [Console text and a UTF-8 plain-text report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes LegionSpace_versions.txt under the skill scripts directory; store-specific results may be version strings, N/A, or error messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
