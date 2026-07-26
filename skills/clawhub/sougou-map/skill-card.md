## Description: <br>
Sougou Map helps agents explain the May 2022 Sogou Maps shutdown and guide migration of legacy code, APIs, and coordinate data to Amap, Baidu Maps, or Tencent Maps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, and users with legacy Sogou Maps references use this skill to identify that the service is discontinued and plan migration to active Chinese map platforms, including API replacement and coordinate-system conversion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map-platform migration advice or provider API details may become outdated. <br>
Mitigation: Verify current Amap, Baidu Maps, and Tencent Maps documentation before making production changes. <br>
Risk: Incorrect coordinate-system conversion can shift legacy locations during migration. <br>
Mitigation: Use official provider conversion APIs and test representative coordinate data before switching platforms. <br>


## Reference(s): <br>
- [Sougou Map on ClawHub](https://clawhub.ai/zhangifonly/skills/sougou-map) <br>
- [Amap Open Platform](https://lbs.amap.com) <br>
- [Baidu Maps Open Platform](https://lbsyun.baidu.com) <br>
- [Tencent Maps Open Platform](https://lbs.qq.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown prose with comparison tables and migration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable behavior; provider API details should be verified before production migration.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
