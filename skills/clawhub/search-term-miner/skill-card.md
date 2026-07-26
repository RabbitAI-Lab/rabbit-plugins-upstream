## Description: <br>
Search Term Miner helps agents analyze paid-ad search-term exports to harvest converting queries into keywords or ad groups, build negative-keyword lists, rank spend-wasting n-grams, and produce an add / negate / move maintenance diff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketers, growth teams, and ad-operations practitioners use this skill on a recurring cadence to turn fresh search-term exports into keyword additions, negative-keyword actions, waste analysis, and a spend-efficiency handoff summary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads ad search-term exports that may include cost, conversion, and account-performance data. <br>
Mitigation: Review and minimize shared export columns before use, and handle generated summaries as business-sensitive ad-performance records. <br>
Risk: Keyword additions, moves, or negative-keyword recommendations could reduce campaign reach or misclassify valuable queries if applied without review. <br>
Mitigation: Treat the maintenance diff as proposed changes and have an account owner review thresholds, match types, and campaign scope before applying them in an ad platform. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown report with maintenance-diff rows, keyword and negative-keyword lists, n-gram waste rankings, score notes, and a handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save a reusable local summary under memory/ad/search-term-miner/ after user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
