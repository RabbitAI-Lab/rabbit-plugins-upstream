## Description: <br>
文曲·发布 prepares Chinese drafts for public release by cleaning internal drafting markers, generating title and summary options, optionally coordinating cover art, and writing a local publish directory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and content teams use this skill to turn Chinese article, report, tutorial, project-introduction, or explanatory drafts into local publication-ready outputs. It is intended for preparing cleaned Markdown, release metadata, title candidates, summaries, and optional cover-art prompts before manual publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads draft content and local wenqu metadata, then writes publish-version files and a changelog entry in the workspace. <br>
Mitigation: Run it only in the intended project workspace and review generated paths and files before using them for publication. <br>
Risk: Optional cover generation delegates behavior to the separate wenqu-image skill. <br>
Mitigation: Review wenqu-image separately before enabling cover generation, and skip or manually replace cover art when that skill is unavailable or unsuitable. <br>
Risk: Online platform publishing is documented only as a future extension and should not occur automatically in this release. <br>
Mitigation: Treat generated outputs as local publication assets and require explicit user confirmation and separate platform-specific review before any public push. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-publish) <br>
- [OpenClaw homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-publish) <br>
- [Project homepage](https://github.com/gogoingai/wenqu-skills) <br>
- [Workflow reference](references/workflow.md) <br>
- [Title and summary reference](references/title-summary.md) <br>
- [Cover prompt reference](references/cover-prompt.md) <br>
- [Auto-publish extension note](references/auto-publish.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown files and text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a local publish directory with a cleaned article Markdown file and meta.md release metadata; optional cover art depends on the separate wenqu-image skill.] <br>

## Skill Version(s): <br>
0.1.19 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
