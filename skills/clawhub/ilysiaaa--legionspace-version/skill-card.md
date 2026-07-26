## Description: <br>
Checks the latest LegionSpace (com.tongfudun.legion) app version across Apple App Store, Tencent MyApp, Xiaomi, vivo, Honor, Huawei, and OPPO stores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ilysiaaa](https://clawhub.ai/user/ilysiaaa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query current LegionSpace app versions across major Chinese app stores and produce a local version report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run Bash and install Python/browser dependencies at runtime. <br>
Mitigation: Run it in a constrained environment and review dependency installation before execution. <br>
Risk: The workflow forces direct network access and bypasses configured proxy settings. <br>
Mitigation: Remove or revise the proxy-bypass settings when organizational network policy requires proxy use or egress controls. <br>
Risk: The embedded Playwright launch arguments include reduced Chromium sandboxing. <br>
Mitigation: Prefer normal Chromium sandboxing where possible, or execute the skill only inside an isolated disposable environment. <br>
Risk: The skill contacts several external app-store sites and may return incomplete results when pages are blocked, slow, or phone-only. <br>
Mitigation: Allowlist expected endpoints where appropriate and treat missing or N/A store results as requiring manual confirmation. <br>


## Reference(s): <br>
- [Legionspace Version on ClawHub](https://clawhub.ai/ilysiaaa/skills/legionspace-version) <br>
- [Apple App Store lookup endpoint](https://itunes.apple.com/lookup?bundleId=com.tongfudun.legion&country=cn) <br>
- [Tencent MyApp LegionSpace page](https://a.app.qq.com/o/simple.jsp?pkgname=com.tongfudun.legion) <br>
- [Xiaomi App Store LegionSpace page](https://app.mi.com/details?id=com.tongfudun.legion) <br>
- [vivo App Store LegionSpace page](https://h5.appstore.vivo.com.cn/period2/index.html#/details?search_word=%E5%A4%A7%E7%BE%A4%E7%A9%BA%E9%97%B4&search_action=4&app_id=4072610&app_pos=1&source=5&appId=4072610&frompage=searchResultApp&listpos=1) <br>
- [Honor App Store LegionSpace page](https://appmarket-h5.cloud.honor.com/h5/share/latest/index.html?shareId=2074329936971526144&shareTo=wechat) <br>
- [Huawei AppGallery LegionSpace page](https://appgallery.huawei.com/app/C114551451?sharePrepath=ag&locale=zh_CN&source=appshare&subsource=C114551451&shareTo=weixin&shareFrom=appmarket&shareIds=958675a106bd4db490a7bb0bbb0e8462_1&callType=SHARE) <br>
- [OPPO App Store search](https://store.oppo.com/cn/search?q=LegionSpace) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Text, Files] <br>
**Output Format:** [Markdown instructions with bash and Python code blocks; runtime output is console text plus a LegionSpace_versions.txt report file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow may install Python requests, Playwright, and Chromium, then contact seven external app-store endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
