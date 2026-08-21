## Description:

Prompt The Browser Company's Dia from the command line and get its answer back as an exact text file for reading or researching logged-in or JavaScript-heavy pages in a local browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[germankovacevic-lab](https://clawhub.ai/user/germankovacevic-lab)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to delegate read-only browser research tasks to a locally running Dia assistant, especially for logged-in or JavaScript-heavy pages where normal fetch tools are insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process logged-in, paywalled, personal, corporate, or regulated browser content.

Mitigation: Review prompts before use, confirm the data is appropriate for Dia to inspect, and store returned plaintext files in a controlled location.

Risk: Fallback or broad output discovery may surface an unrelated Dia output file.

Mitigation: Prefer --no-fallback for sensitive use and adapt the tool to restrict discovery to exact filenames and the current conversation context.

Risk: Unofficial UI automation can break when Dia changes its window or Accessibility behavior.

Mitigation: Re-test against a live Dia install after updates and treat failures as requiring manual review before continued use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/germankovacevic-lab/skills/dia-ask)
- [Dia Browser](https://www.diabrowser.com/)
- [AgentNeo](https://agneo.app)

## Skill Output:

**Output Type(s):** [text, markdown, json, csv]

**Output Format:** [One stdout file path pointing to a Dia-written md, txt, json, or csv file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires macOS, a local Dia session, Accessibility permission, and Node.js; returned files persist as plaintext.]

## Skill Version(s):

0.1.3 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
