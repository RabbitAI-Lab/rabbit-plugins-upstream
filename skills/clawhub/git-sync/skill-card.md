## Description: <br>
git-sync automates skill and agent publishing across Gitee, GitHub, ClawHub, SkillHub, and PyPI with LLM-assisted file filtering and sanitization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and release maintainers use git-sync to synchronize, package, publish, and create releases for skills and agents across configured repositories and marketplaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use publishing authority to push, publish, and create releases across external services. <br>
Mitigation: Install only when that authority is intended; run it in an isolated workspace or account and review config.json, remotes, and release or marketplace flags before execution. <br>
Risk: Security evidence flags review needs around local credentials, shell-based publisher calls, global git credential changes, and cleanup boundaries. <br>
Mitigation: Avoid plaintext or URL-embedded credentials and do not use the skill on untrusted projects until those areas are fixed or explicitly reviewed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ldxs001/skills/git-sync) <br>
- [Usage Guide](artifact/references/guide.md) <br>
- [Command Reference](artifact/references/reference.md) <br>
- [Permissions and Test Report](artifact/references/permissions.md) <br>
- [Blueprint Rules](artifact/references/blueprint_rules.md) <br>
- [Changelog](artifact/references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown status summaries with inline shell commands and generated repository, package, README, ZIP, release, or publication artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write to configured local repositories and invoke external publication services when the relevant release or marketplace flags are used.] <br>

## Skill Version(s): <br>
2.45.0 (source: SKILL.md frontmatter, _meta.json, changelog released 2026-08-04, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
