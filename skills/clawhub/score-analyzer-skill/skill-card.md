## Description: <br>
Analyzes student score data from Excel files and generates professional score-analysis reports with cleaned data, statistics, charts, and packaged report outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Educators, school analysts, and developers use this skill to turn authorized Excel score sheets into cleaned datasets, statistical diagnostics, charts, and narrative Markdown, Word, and HTML reports for exam performance review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that the skill asks agents to run local scripts that are not included in the artifact. <br>
Mitigation: Review and supply trusted scripts in the workspace before allowing any python3 scripts/*.py command to run. <br>
Risk: The security scan notes a possible apt install font step for Chinese chart rendering. <br>
Mitigation: Allow system font installation only in an environment where installing fonts-noto-cjk is intentional. <br>
Risk: The skill processes student score data, which may include sensitive educational records. <br>
Mitigation: Use a dedicated workspace and only process student data the user is authorized to analyze. <br>


## Reference(s): <br>
- [Server-resolved GitHub repository](https://github.com/flyboat403/score-analyzer-skill) <br>
- [Score Analyzer ClawHub page](https://clawhub.ai/flyboat403/skills/score-analyzer-skill) <br>
- [Analysis prompt reference](artifact/references/analysis_prompt.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Files] <br>
**Output Format:** [Markdown reports, Python command snippets, generated charts, Word and HTML reports, and ZIP package files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires authorized Excel score data and local Python dependencies; expected report outputs include validated chart placeholders and packaged report artifacts.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
