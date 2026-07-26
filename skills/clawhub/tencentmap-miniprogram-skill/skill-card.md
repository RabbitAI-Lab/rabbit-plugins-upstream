## Description: <br>
Provides guidance, examples, and API references for building Tencent Map features in WeChat Mini Programs, including map components, location services, markers, route planning, geocoding, POI search, clustering, and visualization layers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to get Tencent Map and WeChat Mini Program guidance, code examples, API parameter explanations, permission notes, and best practices for map and location features. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional temporary-key flow collects a phone number and SMS verification code and can store the phone number and Tencent Map key locally in plaintext. <br>
Mitigation: Use the Tencent console directly for key creation when possible, provide SMS codes only when intentionally using the temporary-key flow, and delete ~/.tencentmap/tempkey.json when the stored record is no longer needed. <br>
Risk: Generated map and location code can request user location data or configure Tencent Location Service keys incorrectly. <br>
Mitigation: Review generated permission declarations, API parameters, key handling, and production authorization requirements before deploying a WeChat Mini Program. <br>


## Reference(s): <br>
- [Tencent Map Mini Program Skill Page](https://clawhub.ai/tencent-adm/skills/tencentmap-miniprogram-skill) <br>
- [Quick Start and Best Practices](artifact/tencentmap-miniprogram-skill/quick_start_and_best_practices.md) <br>
- [Tencent Map Component Guide](artifact/tencentmap-miniprogram-skill/references/map_component_guide.md) <br>
- [MapContext API Overview](artifact/tencentmap-miniprogram-skill/references/mapContext_api/MapContext.md) <br>
- [WeChat Mini Program Map Component Documentation](https://developers.weixin.qq.com/miniprogram/dev/component/map.html) <br>
- [WeChat Location API Documentation](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.getLocation.html) <br>
- [Tencent Location Service](https://lbs.qq.com/) <br>
- [Tencent Location Service Mini Program JavaScript SDK](https://lbs.qq.com/miniProgram/js/jsSdk/jsSdkGuide/jsSdkGuide) <br>
- [Temporary Key Guide](artifact/tencentmap-miniprogram-skill/tempkey-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include WeChat Mini Program WXML, JavaScript, WXSS, JSON configuration, Tencent Map API guidance, and optional temporary-key setup steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
