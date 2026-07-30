## Description: <br>
Adds captions or subtitles to existing single-subject talking-head videos without editing the footage, supporting verbatim caption rails, scene-embedded cinematic captions, VFX captions, and catalog-based visual identities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to add readable and stylized captions to trusted single-subject talking-head videos while preserving the source footage except for documented themed effects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review marks the release suspicious because the skill may update installed skills and use remote or runtime code paths broader than users may expect. <br>
Mitigation: Install only in trusted workspaces, review the skill before use, and run it on non-sensitive media unless local transcript logs and caches are acceptable. <br>
Risk: Theme mode can alter the whole output frame rather than only adding captions. <br>
Mitigation: Review Theme mode choices and preview frames before rendering or publishing output. <br>
Risk: The workflow may fetch packages or models, open local project HTML in Chromium, and contact a CDN during rendering. <br>
Mitigation: Run it in an environment where those network and local execution behaviors are acceptable and review generated project files before publishing outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/embedded-captions) <br>
- [Catalog](artifact/CATALOG.md) <br>
- [Rail reference](artifact/references/rail.md) <br>
- [Composition craft](artifact/references/composition-craft.md) <br>
- [Failure modes](artifact/references/failure-modes.md) <br>
- [Theme authoring](artifact/themes/README.md) <br>
- [DNA authoring](artifact/dna/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration snippets, and generated project files when the local workflow is executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow can produce local media project artifacts and rendered captioned video outputs.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
