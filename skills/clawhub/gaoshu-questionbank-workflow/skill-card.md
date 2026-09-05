## Description:

高数题库批量出题工作流：选章→撞车排查→生成→分布校验→双维度去重→入库→复核→归档

This skill is ready for commercial/non-commercial use.

## Publisher:

[daigxok](https://clawhub.ai/user/daigxok)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and question-bank maintainers use this skill to generate, validate, de-duplicate, import, verify, and archive batches of advanced mathematics questions for a structured local repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can guide an agent to modify local question-bank data, mark imported questions as reviewed, and retain batch artifacts.

Mitigation: Install it only for the intended question-bank project, review generated questions, and inspect backups before importing into the master database.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow instructions for local repository files and question-bank batch artifacts.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
