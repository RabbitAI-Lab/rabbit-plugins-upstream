## Description: <br>
Translates and localizes text, software strings, documents, subtitles, and marketing copy between any language pair. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to translate, review, and localize content across documents, UI string catalogs, subtitles, web pages, games, and regulated text. It helps preserve locale, register, terminology, placeholders, formatting, and review gates while producing target-language deliverables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local translation memory, job records, contacts, project pointers, and subscription notes may retain sensitive working context under ~/Clawic/data/. <br>
Mitigation: Review those local files periodically and avoid retaining confidential source text, personal data, or secrets unless a deliberately sanitized reference is needed. <br>
Risk: Machine translation or CAT workflows can disclose source text to a third-party service. <br>
Mitigation: State what content would leave the machine before using MT, and use local, contracted, or no-MT workflows for confidential, personal, legal, medical, or NDA-covered material. <br>
Risk: Legal, medical, financial, certified, or safety-related mistranslations can create serious downstream harm. <br>
Mitigation: Use jurisdiction-appropriate certification or a qualified second reviewer, verify numbers and obligations separately, and avoid machine translation for regulated content. <br>
Risk: Credentials for MT, CAT, TMS, or localization platforms could be accidentally stored with local translation records. <br>
Mitigation: Store only credential pointers such as environment variable or password-manager references, never secret values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/translate) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Translate page](https://clawic.com/skills/translate) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Software strings guidance](artifact/software-strings.md) <br>
- [Machine translation and post-editing guidance](artifact/machine-translation.md) <br>
- [Regulated work guidance](artifact/legal-medical.md) <br>
- [Quality review guidance](artifact/quality.md) <br>
- [Working file templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Plain text or Markdown, with structured tables and code or configuration snippets when the requested translation workflow needs them.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include translated text, bilingual tables, localization briefs, LQA reports, glossary entries, style guidance, or string catalog fragments.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
