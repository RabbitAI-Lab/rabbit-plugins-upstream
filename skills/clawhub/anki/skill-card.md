## Description: <br>
Helps agents create, repair, and troubleshoot Anki decks, including card writing, deck options, retention problems, imports, sync, and exam-focused planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn source material into Anki-ready cards, tune deck options, diagnose retention and workload problems, handle imports and sync prompts, and plan fixed-date study work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local preference and memory files may retain study settings or context. <br>
Mitigation: Use the disclosed ~/Clawic/data/anki/ folder only for stated preferences or observed context, and let users inspect or remove those files. <br>
Risk: Imports, deletes, note-type changes, and one-way sync choices can overwrite or lose Anki data if followed without review. <br>
Mitigation: Review those recommendations carefully and make a .colpkg backup before acting on them. <br>
Risk: Generated cards can introduce incorrect, ambiguous, or overly broad review items. <br>
Mitigation: Review card batches before import and verify that each card is atomic, contextual, and worth the long-term review cost. <br>


## Reference(s): <br>
- [ClawHub Anki skill page](https://clawhub.ai/ivangdavila/skills/anki) <br>
- [Clawic Anki skill homepage](https://clawic.com/skills/anki) <br>
- [Setup guidance](artifact/setup.md) <br>
- [Memory template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance with optional import-ready card batches and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local Anki preference and memory files under ~/Clawic/data/anki/ when the user provides preferences or context.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
