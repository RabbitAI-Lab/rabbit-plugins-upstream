## Description:

Interview helps users prepare for job interviews with company research, STAR story building, mock interview practice, salary preparation, and follow-up drafting while avoiding job-offer guarantees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agistack](https://clawhub.ai/user/agistack)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and career-support agents use this skill to organize interview preparation, create company research briefs, structure behavioral stories, practice interview responses, prepare salary conversations, and draft follow-up messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Interview stories, company targets, role information, salary notes, and follow-up details may contain sensitive personal or employer information and are stored locally as plaintext.

Mitigation: Use the skill only on trusted machines and backups, avoid entering confidential employer information, and review or delete files under ~/.openclaw/workspace/memory/interview when no longer needed.

Risk: Live company or salary research may use external search tools and disclose query context outside the local workspace.

Mitigation: Explicitly limit external research when needed and review research queries before allowing the agent to use network-backed tools.

Risk: Interview preparation guidance can be incomplete or misleading if treated as a guarantee of hiring outcomes or a replacement for genuine preparation.

Mitigation: Use outputs as preparation aids, verify factual claims, keep responses truthful, and do not rely on the skill to guarantee job offers.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and local JSON files produced by bundled scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores interview preparation notes under local plaintext files in the user's OpenClaw workspace.]

## Skill Version(s):

3.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
