## Description:

Researches public Xiaohongshu/XHS/RedNote notes through SocialDataX for content angles, keyword research, trend material, competitor observation, and sample reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run read-only XHS note searches with a SocialDataX API key and turn returned public note data into content research reports, including sample tables, title hooks, content angles, engagement signals, reusable topics, full note URLs, and complete note IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external SocialDataX service, npm package, and SOCIALDATAX_API_KEY for data calls.

Mitigation: Before installation or use, confirm trust in the SocialDataX service and package, and manage the API key through the documented SocialDataX homepage.

Risk: Research keywords and API credentials are used for external data calls.

Mitigation: Use an appropriate API key for the intended account and avoid submitting sensitive research terms unless that external processing is acceptable.

Risk: Outputs may be incomplete or misleading if treated as full-platform coverage or deterministic traffic guidance.

Mitigation: Interpret results only within the current keyword, filters, and returned page range, and review conclusions before using them for decisions.

## Reference(s):

- [SocialDataX API access and homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-content-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown content research report with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve returned note URLs exactly, including xsec_token query parameters, and copy complete 24-character lowercase hexadecimal note IDs.]

## Skill Version(s):

0.1.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
