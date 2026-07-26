## Description: <br>
Build and drill spaced-repetition packs with recallit by turning PDFs, URLs, repositories, or concepts into source-grounded flashcards and running review through the CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryanwaits](https://clawhub.ai/user/ryanwaits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and learners use this skill to author source-grounded flashcard packs from documents, URLs, repositories, or concepts, then drill due cards through the recallit CLI while letting the engine grade responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill adds bun and the third-party recallit CLI to the agent environment. <br>
Mitigation: Install only in environments where adding those binaries is acceptable, and review the package source and release before use. <br>
Risk: Flashcard packs installed from GitHub, git, npm, or tarballs may contain untrusted third-party content. <br>
Mitigation: Install only packs the user requested, review their source, and treat web-grounded or third-party packs like other untrusted dependencies. <br>
Risk: The substring gate confirms cited text is present in the source, but does not prove that every answer correctly interprets the cited text. <br>
Mitigation: Describe cards as source-cited rather than fully verified, and review flagged or high-impact cards before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ryanwaits/skills/recallit) <br>
- [Publisher profile](https://clawhub.ai/user/ryanwaits) <br>
- [npm package @waits/recallit](https://www.npmjs.com/package/@waits/recallit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to produce recallit pack files such as manifest.json, cards.json, and source text, then use recallit CLI commands for gating, installation, review, and grading.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
