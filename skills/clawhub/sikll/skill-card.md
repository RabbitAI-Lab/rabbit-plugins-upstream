## Description: <br>
复讲/讲经评分与评价助手。输入复讲录音转写文本（或音频/视频），自动分类（义理/历史/仪轨/故事）；无参考资料时自动检索天台藏与大藏经CBETA或联网比对原文后再评价；按"两类×三阶×十项"框架打分，生成带评分依据、祖师参考、失分点解析与提升建议的专业评价报告。鼓励比喻/公案/故事/生活举例/个人体悟，对逻辑散乱给出具体指导。可选音频语气语调节奏分析（第三方语音评测API）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gouchunlei2-png](https://clawhub.ai/user/gouchunlei2-png) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
External users and instructors use this skill to evaluate Buddhist lecture retellings or sermons from text, audio, or video transcripts. It classifies the content, compares it with supplied or retrieved source material, scores it against a structured rubric, and returns an evidence-based improvement report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Religious lecture recordings, videos, transcripts, or extracted topics may be processed through ASR, knowledge-base search, public web lookup, or optional speech-evaluation APIs. <br>
Mitigation: Add explicit user consent before external processing and disclose provider lists, retention and deletion practices, and whether network lookup is enabled. <br>
Risk: Private or identifiable recordings may be sent to external services without clear data-handling limits. <br>
Mitigation: Offer a no-network or local-only mode for sensitive material and require review before handling identifiable recordings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gouchunlei2-png/skills/sikll) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown evaluation report with scores, source-comparison notes, risks, strengths, and improvement suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include optional audio-expression analysis when a third-party speech-evaluation result is provided.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter, CHANGELOG, clawhub.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
