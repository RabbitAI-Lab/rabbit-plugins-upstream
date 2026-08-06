## Description: <br>
Camera snapshot and monitoring skill for OpenClaw: capture, compare, and manage camera snapshots with automated detection and alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators can use this skill to work with camera snapshot workflows, compare images, configure watch mode, and reason about alerts for motion or scene changes. Review the package carefully because the release evidence says the included local tooling is mostly publishing automation rather than the advertised camera implementation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package advertises camera capture and monitoring, but release evidence says the shipped local tooling is mostly publishing automation. <br>
Mitigation: Review the package before installing and verify that any camera command implementation exists and matches the intended use. <br>
Risk: Helper scripts and git hooks may publish to ClawHub, modify version files, or use repository credentials when run. <br>
Mitigation: Do not symlink scripts/camsnap, install the pre-push hook, or run release and autopublish scripts unless you intentionally want maintainer-side publishing automation. <br>


## Reference(s): <br>
- [CamSnap ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/camsnap) <br>
- [terrycarter1985 publisher profile](https://clawhub.ai/user/terrycarter1985) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe JSON output formats for capture and diff commands.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata, SKILL.md frontmatter, _meta.json, and CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
