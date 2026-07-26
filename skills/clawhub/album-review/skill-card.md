## Description: <br>
Deep, source-traceable long-form Chinese album review for a named music credit and album, producing one comprehensive critique while routing away gear, buying, and lyric-only requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and reviewers use this skill to produce source-traceable Chinese long-form critiques for albums when they can provide a primary artist, composer, conductor, band, or performer plus an album name. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use external search for album research, which can expose private or unreleased music materials if the user provides them. <br>
Mitigation: Avoid using the skill with private or unreleased materials, or run it in offline/caller-supplied mode when external search is not acceptable. <br>
Risk: Album reviews can contain incorrect discographic facts if public sources are thin or conflicting. <br>
Mitigation: Use the backing JSON and validation scripts to require source IDs for fact-class claims, and record unresolved gaps instead of inventing missing details. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/vincentjiang06/skills/album-review) <br>
- [Skill specification](artifact/SKILL.md) <br>
- [Research protocol](artifact/rules/research-protocol.md) <br>
- [Output template](artifact/rules/output-template.md) <br>
- [Music source roster](artifact/references/source-roster.md) <br>
- [Backing JSON schema](artifact/schemas/backing.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Chinese Markdown review plus backing JSON and an evidence appendix] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets a 10,000-15,000 CJK-character review; fact-class claims are expected to trace to evidence[] in the backing JSON.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
