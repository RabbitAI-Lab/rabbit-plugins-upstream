## Description: <br>
Chaoxing Auto Grade helps teachers download Chaoxing MOOC homework review HTML, extract subjective questions, grade answers through a configured LLM API, write scores back into local HTML, and produce cleaned grading summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenghaozhangswu](https://clawhub.ai/user/chenghaozhangswu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teachers and education operations staff use this skill to automate Chaoxing homework collection, subjective-answer scoring, score write-back, and cleaned HTML report generation. It is intended for workflows where the operator can review student data handling and manually audit AI-generated grades. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles Chaoxing teacher login access and may encourage storing real credentials in config.json. <br>
Mitigation: Use a dedicated browser profile, avoid storing real passwords in config.json, and review login configuration before running the download step. <br>
Risk: Student submissions may be sent to the configured external AI provider for subjective grading. <br>
Mitigation: Confirm that sending student work to the provider is permitted, use an approved provider and API key, and manually audit AI-generated grades before relying on them. <br>
Risk: Score write-back modifies local homework HTML files in place. <br>
Mitigation: Keep backups, restrict input and output directories, and test on copied files before applying scores to the main working set. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenghaozhangswu/skills/chaoxing-auto-grade) <br>
- [Chaoxing MOOC service endpoint](https://mooc2-ans.chaoxing.com) <br>
- [Sensenova chat completions endpoint](https://token.sensenova.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with Python commands, JSON configuration, local JSON intermediates, modified HTML files, and cleaned HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local homework HTML downloads, subj_questions.json, subj_graded.json, in-place score updates, and cleaned HTML output directories.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
