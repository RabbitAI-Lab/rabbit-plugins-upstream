## Description: <br>
Helps agents publish and synchronize local skills to ClawHub and Tencent SkillHub using allowlists, version checks, filtered temporary publish directories, and platform-specific release commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cat-xierluo](https://clawhub.ai/user/cat-xierluo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to prepare, verify, and publish local skill directories to ClawHub or Tencent SkillHub. It is intended for release management workflows that need platform routing, version tracking, and protection against accidental upload of ignored local configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing workflows can upload local skill contents to public hubs, including unintended files if the working tree or filters are wrong. <br>
Mitigation: Inspect the prepared temporary publish directory before publishing and keep private configuration, tokens, customer data, and case files out of publishable skill directories. <br>
Risk: The workflow depends on authenticated ClawHub or SkillHub CLI sessions and may affect public release state. <br>
Mitigation: Confirm the active CLI account before publishing, use dry-run or whoami checks when available, and avoid storing API tokens in configuration files. <br>
Risk: Platform routing and license rules can cause a skill to be sent to the wrong hub or released under unexpected terms. <br>
Mitigation: Review the allowlist, license field, target platform, version, and changelog before executing publish commands. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/cat-xierluo/skills/clawhub-sync) <br>
- [Project homepage](https://github.com/cat-xierluo/legal-skills) <br>
- [ClawHub CLI documentation](https://docs.openclaw.ai/clawhub/cli) <br>
- [ClawHub Skill Format documentation](https://docs.openclaw.ai/clawhub/skill-format) <br>
- [Tencent SkillHub publishing tutorial](https://skillhub.cn/tutorials#publish-via-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with shell commands, YAML examples, and helper script guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to create filtered temporary publish directories, run platform CLIs, and update local sync records.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release evidence, SKILL.md frontmatter, CHANGELOG.md released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
