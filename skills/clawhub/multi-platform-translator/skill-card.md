## Description: <br>
Translate content across multiple platforms and languages with context-aware localization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to translate Chinese and English content with a selected web translation provider, context-aware localization workflow, terminology checks, and review guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text submitted for translation may be sent to an outside translation provider or logged-in chat service. <br>
Mitigation: Do not use this skill for secrets, regulated data, internal business documents, contracts, or legal text unless the user is comfortable sending the text to the selected provider. <br>
Risk: The artifact claims translation content only travels through the local browser, while server security evidence warns that content is submitted to outside services. <br>
Mitigation: Prefer explicit provider selection and user consent before each translation, and treat provider privacy terms as authoritative. <br>
Risk: Translation quality and availability can vary by provider, login state, and network access. <br>
Mitigation: Cross-check important translations, preserve terminology requirements, and have high-impact or specialized content reviewed by a qualified domain reviewer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/multi-platform-translator) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>
- [iFlytek translation](https://fanyi.xfyun.cn/console/trans/text) <br>
- [DeepL Translator](https://www.deepl.com/zh/translator) <br>
- [iCIBA](https://www.iciba.com/) <br>
- [Doubao chat](https://www.doubao.com/chat) <br>
- [Tencent Yuanbao chat](https://yuanbao.tencent.com/chat/naQivTmsDa) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain text translation results with optional translation brief, draft, review notes, terminology flags, and provider error guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use browser-based third-party translation or chat services selected by the user; provider availability, login state, and network access can affect results.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
