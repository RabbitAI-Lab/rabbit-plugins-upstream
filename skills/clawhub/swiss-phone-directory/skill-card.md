## Description: <br>
Swiss phone directory lookup via search.ch API for businesses, people, reverse phone lookup, addresses, and business categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xenofex7](https://clawhub.ai/user/xenofex7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to search Swiss phone directory records, find contact details for Swiss businesses or people, reverse-lookup phone numbers, and retrieve address or category details through search.ch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lookup queries and the SEARCHCH_API_KEY are sent to search.ch. <br>
Mitigation: Install only if this data sharing is acceptable, use a dedicated API key, and avoid logging or sharing outputs that reveal sensitive queries or credentials. <br>
Risk: Configuration examples include shell profiles and gateway environment settings that can expose credentials if copied into shared files. <br>
Mitigation: Prefer a secret manager or temporary environment variable, and keep API keys out of shared dotfiles, screenshots, logs, and repository files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xenofex7/skills/swiss-phone-directory) <br>
- [search.ch telephone API](https://search.ch/tel/api/) <br>
- [search.ch telephone API help](https://search.ch/tel/api/help.en.html) <br>
- [search.ch API key request](https://search.ch/tel/api/getkey.en.html) <br>
- [search.ch API terms](https://search.ch/tel/api/terms.en.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown-formatted CLI output or JSON, with configuration guidance and shell commands in documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SEARCHCH_API_KEY; queries and API key are sent to search.ch.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
