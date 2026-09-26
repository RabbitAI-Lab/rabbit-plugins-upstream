## Description: <br>
Reddit Research helps an agent extract and summarize Reddit trends, recurring questions, and content gaps for keyword analysis and search traffic optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and SEO researchers use this skill to analyze targeted Reddit discussions for trending topics, recurring user problems, and content opportunities. It is positioned for keyword research, ranking improvement, and search traffic optimization, not black-hat SEO. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command and file-access tools without clearly limiting how they will be used. <br>
Mitigation: Install and run it only in a sandboxed agent profile with narrow workspace access and review proposed commands before execution. <br>
Risk: The skill may require API credentials for Reddit or another service, but the artifact does not clearly document the exact service, command behavior, or what data may leave the environment. <br>
Mitigation: Do not provide real credentials or sensitive local files until the publisher documents the required service, allowed commands, and outbound data handling. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown or JSON research summaries with execution metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include research results, research metadata, status, and an execution log.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
