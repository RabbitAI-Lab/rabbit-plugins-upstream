## Description: <br>
Global Skill Daily scans ClawHub and SkillHub every three days, recommends skills across ten dimensions, and saves a generated digest to configured destinations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to monitor public skill ecosystems, compare Chinese and global trends, and receive a recurring Markdown digest with recommendations. It can optionally use local agent context to personalize recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill scans sensitive local context by default and the authoritative security summary states that published reports may still contain context-derived signals. <br>
Mitigation: Run with --dry-run first, inspect generated user_context and recommendation files, and use --no-context-scan in privacy-sensitive environments. <br>
Risk: Generated digests can be published to external destinations such as Feishu and IMA when credentials are configured. <br>
Mitigation: Disable destinations that are not needed with --no-feishu, --no-ima, and --no-obsidian, and use least-privilege credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/global-skill-daily) <br>
- [Project homepage](https://github.com/trae-solo/global-skill-daily) <br>
- [Pain points reference](artifact/references/pain-points.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown digest with JSON data files and delivery status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write local files and push digests to Obsidian, IMA, and Feishu when credentials and destination flags are enabled.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
