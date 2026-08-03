## Description: <br>
Transcript Crafter turns interview or meeting transcripts into WeChat public-account long-form articles through structured extraction, persona adaptation, outlining, search-backed enrichment, fact checking, and rewriting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, editors, and communications teams use this skill to transform interviews, meeting transcripts, or source articles into polished long-form WeChat articles with structured source extraction, supplemental research, fact checks, and publication-oriented formatting. It is not intended for original ideation from scratch, trend posts, or pure translation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can save transcript-derived content to the user's Desktop and upload it to Feishu cloud storage. <br>
Mitigation: Before use, decide whether cloud upload is acceptable for the material; explicitly instruct the agent not to upload to Feishu when handling confidential or restricted transcripts. <br>
Risk: The workflow can rely on external search services and supplemental research, which may expose sensitive transcript topics or context. <br>
Mitigation: Redact confidential details before invoking search-backed enrichment and keep the confirmation checkpoints enabled for sensitive material. <br>
Risk: The workflow can invoke local helper commands and use Feishu-related credentials. <br>
Mitigation: Review configured helper scripts, lark-cli behavior, and FEISHU_APP_ID, FEISHU_APP_SECRET, and FEISHU_USER_OPEN_ID handling before installation or execution. <br>
Risk: All-auto mode skips the normal user confirmation checkpoints for extracted material, article framing, and supplemental research. <br>
Mitigation: Avoid all-auto mode when accuracy, confidentiality, or editorial control matters; require review at the extraction, outline, and research-confirmation stages. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edwardwason/skills/transcript-crafter) <br>
- [Source Quality Gate](references/source-quality-gate.md) <br>
- [Pipeline Detail](references/pipeline-detail.md) <br>
- [Extraction Guide](references/extraction-guide.md) <br>
- [Fact Check Guide](references/fact-check-guide.md) <br>
- [Title Strategist](references/title-strategist.md) <br>
- [WeChat Format Guide](references/wechat-format-guide.md) <br>
- [Tool Router](references/tool-router.md) <br>
- [Quality Checklist](references/quality-checklist.md) <br>
- [Anti-AI Writing Rules](references/anti-ai-rules.md) <br>
- [Interview Personas](references/interview-personas.yaml) <br>
- [khazix-skills Reference](https://github.com/KKKKhazix/khazix-skills) <br>
- [renwei-writing Reference](https://github.com/orange2ai/renwei-writing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown article drafts, structured intermediate notes, source-check tables, file paths, and operational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final articles are targeted at 2500-4000 Chinese characters and formatted for WeChat public-account publishing.] <br>

## Skill Version(s): <br>
1.3.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
