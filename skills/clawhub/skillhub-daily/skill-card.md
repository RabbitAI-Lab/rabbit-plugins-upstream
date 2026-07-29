## Description: <br>
SkillHub Daily scans SkillHub.cn rankings, category searches, and keyword searches to produce daily China-focused skill recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to receive a daily briefing of SkillHub.cn skills selected for China ecosystem fit, active developers, trend signals, memory keyword matches, and optional quality or security evaluations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local memory-derived keywords and uses them to personalize recommendations. <br>
Mitigation: Review the configured TRAE memory path before running; the release evidence says raw memory content is not transmitted and recommendation output records keyword match counts rather than raw keywords. <br>
Risk: The skill can publish generated briefings to configured external destinations. <br>
Mitigation: Use --skip-push for local-only runs, review destination credentials, and only enable Obsidian, IMA, or Feishu publishing intentionally. <br>
Risk: The workflow depends on local command-line tools for SkillHub and optional publishing. <br>
Mitigation: Ensure the skillhub and lark-cli binaries on PATH are trusted before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/skillhub-daily) <br>
- [README](artifact/README.en.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown briefing plus JSON recommendation and snapshot files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write local briefing files and optionally publish to Obsidian, IMA, and Feishu when credentials are configured.] <br>

## Skill Version(s): <br>
7.0.1 (source: server release evidence, frontmatter, and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
