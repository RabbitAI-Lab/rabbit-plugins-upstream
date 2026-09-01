## Description:

AI Career Position helps Chinese job seekers evaluate job descriptions and offers, compare fit, salary, level, fraud and outsourcing risks, generate ATS-friendly Chinese resumes, prepare interviews, and track applications while keeping applications user-driven.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tanchunzhuo](https://clawhub.ai/user/tanchunzhuo)

### License/Terms of Use:

MIT

## Use Case:

External users, especially China-market job seekers, use this skill to structure career direction, job-description review, resume tailoring, interview preparation, offer comparison, and application tracking. It is designed to keep final decisions, submissions, platform actions, and privacy-sensitive data under the user's control.

### Deployment Geography for Use:

Global, with content and market data focused on China

## Known Risks and Mitigations:

Risk: The one-line installer can execute mutable remote code and overwrite existing skill directories without backup or confirmation.

Mitigation: Review install.sh before running it; prefer cloning or downloading a fixed release, inspecting the files, and manually copying the skill.

Risk: The optional bookmarklet captures page text for local inbox use.

Mitigation: Run the bookmarklet only on job-description pages and review captured content before using it.

Risk: The local workspace can contain resumes, salary expectations, interview stories, and application history.

Mitigation: Keep workspace/ private, avoid committing it, and delete local workspace files when they are no longer needed.

## Reference(s):

- [Server-resolved source repository](https://github.com/tanchunzhuo/ai-career-position)
- [ClawHub skill page](https://clawhub.ai/tanchunzhuo/skills/ai-career-position)
- [README](README.md)
- [Privacy and compliance](docs/PRIVACY.md)
- [Value and boundaries](docs/VALUE_AND_BOUNDARIES.md)
- [Data update guidance](docs/DATA_UPDATES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional generated files, HTML/PDF resume artifacts, shell commands, TSV/JSON/YAML workspace records, and local configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps applications and platform actions user-driven; user data is intended to remain in local workspace files.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence); artifact frontmatter reports 1.0.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
