## Description: <br>
Batch add word cards to Anki via AnkiConnect. Supports Spanish-Chinese vocabulary cards with automatic translation and example sentences. Use when the user wants to add multiple words to Anki at once, import vocabulary lists, or bulk-create flashcards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fondas123](https://clawhub.ai/user/fondas123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prepare TSV, JSON, or plain-text vocabulary batches and add them to Anki decks through AnkiConnect. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read user-provided TSV or JSON input files. <br>
Mitigation: Use it only with intended vocabulary files and review generated batch files before import. <br>
Risk: The skill can add persistent notes to an Anki collection through AnkiConnect. <br>
Mitigation: Run dry-run mode first, verify deck and model names, and back up Anki before large imports. <br>


## Reference(s): <br>
- [AnkiConnect](https://foosoft.net/projects/anki-connect/) <br>
- [ClawHub skill page](https://clawhub.ai/fondas123/skills/anki-batch-cards) <br>
- [Publisher profile](https://clawhub.ai/user/fondas123) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with TSV or JSON examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local TSV or JSON input files and reports AnkiConnect import results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
