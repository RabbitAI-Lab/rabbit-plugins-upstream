## Description: <br>
Fetches and presents the Spanish JW daily text from the official Watchtower Online Library site for requests about daily JW or biblical content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[djismgaming](https://clawhub.ai/user/djismgaming) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve the current Spanish JW daily text, including the biblical citation, explanation, and source link. It is intended for requests such as asking for the JW text of the day or daily JW biblical content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The implementation contacts wol.jw.org to fetch the current daily text and the security guidance notes shell-based curl usage. <br>
Mitigation: Install only when network contact with wol.jw.org is acceptable; review the release before deployment and prefer replacing shell-based curl with web_fetch or a native HTTP API. <br>


## Reference(s): <br>
- [Watchtower Online Library Spanish daily text](https://wol.jw.org/es/wol/h/r4/lp-s) <br>
- [Jwdiario ClawHub skill page](https://clawhub.ai/djismgaming/skills/jwdiario) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown] <br>
**Output Format:** [Markdown-formatted Spanish daily text with a source link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches current-day content from wol.jw.org/es and is expected to preserve the Spanish source text without translation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
