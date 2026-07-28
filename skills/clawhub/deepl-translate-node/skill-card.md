## Description: <br>
Uses DeepL's neural machine translation API as a fallback for translations where proper nouns, ambiguous phrasing, specialized terminology, idioms, low-resource language pairs, or high-stakes use make mistranslation costly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rockbenben](https://clawhub.ai/user/rockbenben) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to call DeepL when direct model translation is uncertain or when the user explicitly asks for DeepL translation. It is intended for passages where terminology, ambiguity, idioms, low-resource language pairs, or publication risk make translation quality important. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires storing a DeepL API key in the environment. <br>
Mitigation: Set DEEPL_API_KEY only in trusted environments and never hardcode or expose the key. <br>
Risk: Text submitted for translation is sent to DeepL. <br>
Mitigation: Use the skill only for content that may be shared with DeepL under the user's data handling requirements. <br>
Risk: An unsafe DEEPL_API_HOST value could send requests away from the intended DeepL endpoint. <br>
Mitigation: Keep DEEPL_API_HOST unset or set it only to the official DeepL Free or Pro host. <br>


## Reference(s): <br>
- [DeepL supported languages documentation](https://developers.deepl.com/docs/getting-started/supported-languages) <br>
- [DeepL languages API endpoint for translate_text](https://api-free.deepl.com/v3/languages?resource=translate_text) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text translation output, with ERROR-prefixed plain text on failure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and DEEPL_API_KEY; requests terminate after a 60-second timeout.] <br>

## Skill Version(s): <br>
1.1.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
