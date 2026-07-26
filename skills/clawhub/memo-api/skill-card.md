## Description: <br>
Memo Api helps agents use the MaiMemo Open API to look up vocabulary, manage definitions, mnemonics, word lists, example sentences, and study data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[celend](https://clawhub.ai/user/celend) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and language-learning users can use this skill to let an agent query MaiMemo vocabulary data and manage the authenticated user's custom definitions, mnemonics, cloud word lists, example sentences, and study progress. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a MaiMemo Open API token that can access the authenticated user's vocabulary and study data. <br>
Mitigation: Install only when the user intends to let an agent use MAIMEMO_TOKEN, keep the token in a trusted environment, and avoid pasting or logging it outside that environment. <br>
Risk: The skill can create, update, delete, add, or advance MaiMemo learning content. <br>
Mitigation: Confirm with the user before any write action, including create, update, delete, add-word, or advance-review requests. <br>
Risk: The skill can export study history through paginated API calls. <br>
Mitigation: Confirm before exporting all study history and handle exported study data as user-sensitive information. <br>
Risk: Study endpoints are beta and may be unavailable or return incomplete daily progress if MaiMemo sync requirements are not met. <br>
Mitigation: Treat study metrics as best-effort, explain beta or sync limitations to the user, and verify important results in MaiMemo before relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/celend/skills/memo-api) <br>
- [MaiMemo Open API Base](https://open.maimemo.com/open/api/v1) <br>
- [MaiMemo Open API Token Page](https://open.maimemo.com/open/api/v1/tokens/openapi) <br>
- [Vocabulary API](references/vocabulary-api.md) <br>
- [Interpretations API](references/interpretations-api.md) <br>
- [Notes API](references/notes-api.md) <br>
- [Notepads API](references/notepads-api.md) <br>
- [Phrases API](references/phrases-api.md) <br>
- [Study API](references/study-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown with curl commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses MAIMEMO_TOKEN and curl to call MaiMemo Open API endpoints.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
