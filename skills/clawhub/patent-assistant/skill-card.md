## Description: <br>
Patent Assistant helps R&D users turn technical ideas into structured patent disclosure drafts and run preliminary patent searches with similarity analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ty-teo](https://clawhub.ai/user/ty-teo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, researchers, and inventors use this skill to draft patent disclosure materials from technical descriptions and perform preliminary multi-source patent searches. It supports early novelty review but does not replace inventor, patent counsel, or formal prior-art review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent search queries may disclose confidential or not-yet-filed invention details to external patent and academic search sites. <br>
Mitigation: Use redacted keywords, avoid sensitive implementation details in external searches, or run only the local disclosure-generation workflow until the inventor or counsel approves external searching. <br>
Risk: Generated disclosures and preliminary search results may be incomplete or unsuitable for filing decisions. <br>
Mitigation: Have the inventor review technical details and use qualified patent counsel or a formal prior-art search before relying on the output. <br>


## Reference(s): <br>
- [Patent Assistant README](artifact/README.md) <br>
- [Patent Assistant Skill Definition](artifact/SKILL.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/ty-teo/skills/patent-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown patent disclosure drafts, text or JSON patent search results, and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write disclosure files when an output path is supplied; patent searches may contact external patent and academic search sites.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
